import json
import os
import unittest

import ioc
import pyotp
import sq.test

from ....infra import orm
from ..endpoints import AuthenticationEndpoint


class PinAuthenticationTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super().setUp()
        self.service = ioc.require('PinService')
        self.repo = ioc.require('PinRepository')
        self.endpoint = AuthenticationEndpoint()
        self.pin = "12345"
        self.service.createpin(self.gsid, self.pin)

    @sq.test.integration
    def test_succesful_authentication_by_totp(self):
        params = {
            'method': 'POST',
            'json': {
                'gsid': self.gsid,
                'factors': [
                    {'using': 'pin', 'factor': self.pin}
                ]
            }
        }
        response = self.request(self.endpoint.handle, **params)
        self.assertEqual(response.status_code, 200, response.response)

    @sq.test.integration
    def test_authentication_for_non_existing_gsid_fails(self):
        params = {
            'method': "POST",
            'json': {
                'gsid': bytes.hex(os.urandom(16)),
                'factors': [
                    {'using': 'pin', 'factor': '54321'}
                ]
            }
        }
        response = self.request(self.endpoint.handle, **params)
        self.assertEqual(response.status_code, 401)

    @sq.test.integration
    def test_authentication_with_invalid_pin_fails(self):
        params = {
            'method': "POST",
            'json': {
                'gsid': self.gsid,
                'factors': [
                    {'using': 'pin', 'factor': '54321'}
                ]
            }
        }
        response = self.request(self.endpoint.handle, **params)
        self.assertEqual(response.status_code, 401)

    @sq.test.integration
    def test_authentication_with_invalid_pin_fails(self):
        params = {
            'method': "POST",
            'json': {
                'gsid': self.gsid,
                'factors': [
                    {'using': 'pin', 'factor': '54321'}
                ]
            }
        }
        response = self.request(self.endpoint.handle, **params)
        self.assertEqual(response.status_code, 401)

    @sq.test.integration
    def test_authentication_with_valid_pin_fails_after_n_failed_attempts(self):
        params = {
            'method': "POST",
            'json': {
                'gsid': self.gsid,
                'factors': [
                    {'using': 'pin', 'factor': '54321'}
                ]
            }
        }
        for i in range(3):
            response = self.request(self.endpoint.handle, **params)

        # The PIN should be blocked now.
        params['json']['factors'][0]['factor'] = self.pin
        response = self.request(self.endpoint.handle, **params)
        self.assertEqual(response.status_code, 401)

    @sq.test.integration
    def test_authentication_with_valid_pin_resets_counter(self):
        params = {
            'method': "POST",
            'json': {
                'gsid': self.gsid,
                'factors': [
                    {'using': 'pin', 'factor': '54321'}
                ]
            }
        }
        for i in range(2):
            response = self.request(self.endpoint.handle, **params)

        dao = self.repo.get(self.gsid)
        self.assertEqual(dao.failed, 2)
        self.assertEqual(response.status_code, 401)

        # The PIN should be blocked now.
        params['json']['factors'][0]['factor'] = self.pin
        response = self.request(self.endpoint.handle, **params)
        self.assertEqual(response.status_code, 200)

        dao = self.repo.get(self.gsid)
        self.assertEqual(dao.failed, 0)


class AuthenticationTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super().setUp()
        self.service = ioc.require('OneTimePasswordService')
        dto = self.service.generate('totp', self.gsid,
            "test@quantumframework.org", "SAFI Test Case")
        self.endpoint = AuthenticationEndpoint()
        self.otp = pyotp.TOTP(dto.secret)

    @sq.test.integration
    def test_succesful_authentication_by_totp(self):
        request = sq.test.request_factory(
            method='POST',
            json={
                'gsid': self.gsid,
                'factors': [
                    {'using': 'otp', 'factor': self.otp.now()}
                ]
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 200, response.response)

    @sq.test.integration
    def test_wrong_authentication_by_totp(self):
        request = sq.test.request_factory(
            method='POST',
            json={
                'gsid': self.gsid,
                'factors': [
                    {'using': 'otp', 'factor': '123456'}
                ]
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 401, response.response)

        dto = json.loads(response.response[0])
        self.assertIn('failed', dto)
        self.assertIn('otp', dto['failed'])

    @sq.test.integration
    def test_unknown_subject_authentication_by_totp(self):
        request = sq.test.request_factory(
            method='POST',
            json={
                'gsid': self.gsid[:-1] + '1',
                'factors': [
                    {'using': 'otp', 'factor': '123456'}
                ]
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 404, response.response)

#pylint: skip-file

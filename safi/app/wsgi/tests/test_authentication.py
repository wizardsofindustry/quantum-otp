import json
import unittest

import ioc
import pyotp
import sq.test

from ....infra import orm
from ..endpoints import AuthenticationEndpoint


class AuthenticationTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(AuthenticationTestCase, self).setUp()
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

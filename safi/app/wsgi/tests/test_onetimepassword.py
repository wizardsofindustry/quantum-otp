import json
import unittest

import ioc
import sq.test
import pyotp

from ....infra import orm
from ..endpoints import OneTimePasswordEndpoint


class OneTimePasswordTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(OneTimePasswordTestCase, self).setUp()
        self.endpoint = OneTimePasswordEndpoint()
        self.otp = ioc.require('OneTimePasswordService')
        self.auth = ioc.require('AuthenticationService')

    @sq.test.integration
    def test_duplicate_otp_non_active_generates_new(self):
        otp = self.otp.generate('totp', self.gsid,
            'test@quantumframework.org',
            "SAFI Test Case")

        request = sq.test.request_factory(
            method='POST',
            accept="application/json",
            json={
                'gsid': self.gsid,
                'nsid': "test@quantumframework.org",
                'issuer': "SAFI Test Case"
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], "application/json")

        dto = json.loads(response.response[0])
        self.assertNotEqual(dto['secret'], otp.secret)

    @sq.test.integration
    def test_duplicate_otp_active_fails(self):
        dto = self.otp.generate('totp', self.gsid,
            'test@quantumframework.org',
            "SAFI Test Case")
        otp = pyotp.TOTP(dto.secret)

        # Authenticate using the OTP to ensure that its enabled.
        self.auth.authenticate(self.gsid, [self.dto(using='otp', factor=otp.now())])

        with self.assertRaises(self.otp.OneTimePasswordActive):
            request = sq.test.request_factory(
                method='POST',
                accept="application/json",
                json={
                    'gsid': self.gsid,
                    'nsid': "test@quantumframework.org",
                    'issuer': "SAFI Test Case"
                }
            )
            response = self.run_callable(self.loop, self.endpoint.handle, request)

    @sq.test.integration
    def test_create_otp_as_link_for_subject(self):
        request = sq.test.request_factory(
            method='POST',
            accept="application/json",
            json={
                'gsid': self.gsid,
                'nsid': "test@quantumframework.org",
                'issuer': "SAFI Test Case"
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], "application/json")

    @sq.test.integration
    def test_create_otp_as_image_for_subject(self):
        request = sq.test.request_factory(
            method='POST',
            accept="image/png",
            json={
                'gsid': self.gsid,
                'nsid': "test@quantumframework.org",
                'issuer': "SAFI Test Case"
            }
        )
        response = self.run_callable(self.loop, self.endpoint.handle, request)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers['Content-Type'], "image/png")


#pylint: skip-file

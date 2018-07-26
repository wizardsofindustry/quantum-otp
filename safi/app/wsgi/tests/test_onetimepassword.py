import json
import unittest

import sq.test

from ....infra import orm
from ..endpoints import OneTimePasswordEndpoint


class OneTimePasswordTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(OneTimePasswordTestCase, self).setUp()
        self.endpoint = OneTimePasswordEndpoint()

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

import json
import unittest

import ioc
import sq.test

from ....infra import orm
from ..endpoints import PinEndpoint


class PinTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(PinTestCase, self).setUp()
        self.endpoint = PinEndpoint()
        self.pin = ioc.require('PinService')

    def test_set_pin(self):
        """Set PIN using default parameters."""
        response = self.request(
            self.endpoint.handle,
            method="POST",
            accept="application/json",
            json={
                'gsid': self.gsid
            }
        )
        self.assertEqual(response.status_code, 201)
        dto = json.loads(response.response[0])
        self.assertIn('pin', dto)

    def test_set_pin_with_user_defined_code(self):
        """Set PIN using default parameters."""
        response = self.request(
            self.endpoint.handle,
            method="POST",
            accept="application/json",
            json={
                'gsid': self.gsid,
                'pin': "12345"
            }
        )
        self.assertEqual(response.status_code, 201)
        dto = json.loads(response.response[0])
        self.assertIn('pin', dto)
        self.assertEqual(dto['pin'], '12345')

    def test_set_pin_fails_if_existing(self):
        """Set PIN using default parameters."""
        params = {
            'method': "POST",
            'accept': "application/json",
            'json': {'gsid': self.gsid}
        }
        self.request(self.endpoint.handle, **params)
        with self.assertRaises(self.pin.DuplicatePinCode):
            self.request(self.endpoint.handle, **params)

    def test_set_pin_not_fails_if_existing_and_force(self):
        """Set PIN using default parameters."""
        params = {
            'method': "POST",
            'accept': "application/json",
            'json': {'gsid': self.gsid, 'force': True}
        }
        self.request(self.endpoint.handle, **params)
        self.request(self.endpoint.handle, **params)


#pylint: skip-file

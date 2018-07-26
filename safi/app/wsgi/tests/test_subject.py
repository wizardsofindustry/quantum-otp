import json
import unittest

import ioc
import pyotp
import sq.test

from ....infra import orm
from ..endpoints import SubjectChallengesEndpoint


class SubjectChallengesTestCase(sq.test.SystemTestCase):
    gsid ="00000000-0000-0000-0000-000000000000"
    metadata = orm.Relation.metadata

    def setUp(self):
        super(SubjectChallengesTestCase, self).setUp()
        self.service = ioc.require('OneTimePasswordService')
        self.service.generate('totp', self.gsid,
            "test@quantumframework.org", "SAFI Test Case")
        self.endpoint = SubjectChallengesEndpoint()

    @sq.test.integration
    def test_otp_is_in_available_challenges(self):
        request = sq.test.request_factory(method='GET')
        response = self.run_callable(self.loop, self.endpoint.handle,
            request, gsid=self.gsid)
        self.assertEqual(response.status_code, 200, response.response)

        dto = json.loads(response.response[0])
        self.assertIn('factors', dto)
        self.assertIn('otp', dto['factors'])

#pylint: skip-file

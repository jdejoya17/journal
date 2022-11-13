# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.http_response import HTTPResponse  # noqa: E501
from swagger_server.models.register_new_user import RegisterNewUser  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAuthenticationController(BaseTestCase):
    """AuthenticationController integration test stubs"""

    def test_login_user(self):
        """Test case for login_user

        
        """
        body = Object()
        response = self.client.open(
            '/api/v1/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_user(self):
        """Test case for logout_user

        
        """
        response = self.client.open(
            '/api/v1/logout',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_user(self):
        """Test case for register_user

        
        """
        body = RegisterNewUser()
        response = self.client.open(
            '/api/v1/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

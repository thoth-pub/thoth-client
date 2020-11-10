#!/usr/bin/env python3
"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""

import json
import urllib
import requests
from .errors import ThothError


class ThothAuthenticator():  # pylint: disable=too-few-public-methods
    """Authentication handler"""
    def __init__(self, auth_endpoint, email, password):
        self.auth_endpoint = auth_endpoint
        self.payload = {'email': email, 'password': password}

    def get_token(self):
        """Perform an authentication request"""
        try:
            response = requests.post(self.auth_endpoint, json=self.payload)
            if response.status_code == 401:
                raise ThothError(self.auth_endpoint, 'Wrong credentials')
            token = response.json()['token']
        except (KeyError, TypeError, ValueError, AssertionError,
                json.decoder.JSONDecodeError, urllib.error.HTTPError):
            raise ThothError(self.auth_endpoint, response)
        return token

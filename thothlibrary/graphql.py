"""
GraphQL transport helpers for Thoth.

Copyright (c) 2026 Thoth Open Metadata
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json

import requests


class GraphQLClientRequests:
    """Minimal GraphQL HTTP client used by the Thoth library."""

    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.token = None
        self.headername = "Authorization"

    def execute(self, query, variables=None):
        """Execute a GraphQL request and return the response body."""
        return self._send(query, variables)

    def inject_token(self, token, headername="Authorization"):
        """Inject an auth token into subsequent requests."""
        self.token = token
        self.headername = headername

    def _send(self, query, variables=None):
        payload = {
            "query": query,
            "variables": variables,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        if self.token is not None:
            headers[self.headername] = str(self.token)

        response = requests.post(
            self.endpoint,
            data=json.dumps(payload).encode("utf-8"),
            headers=headers,
        )
        return response.content.decode("utf-8")

#!/usr/bin/env python3
"""
Token helpers for authenticated Thoth requests.

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


class ThothAuthenticator:  # pylint: disable=too-few-public-methods
    """Compatibility helper for PAT-based authentication."""

    def __init__(self, token):
        self.token = token

    def get_token(self):
        """Return the configured personal access token unchanged."""
        return self.token

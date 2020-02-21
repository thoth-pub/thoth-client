#!/usr/bin/env python3
"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


class ThothError(Exception):
    """Exception to report Thoth errors"""
    def __init__(self, request, response):
        message = "GraphQL Error.\nRequest:\n{}\n\nResponse:\n{}".format(
            request, response)
        super().__init__(message)

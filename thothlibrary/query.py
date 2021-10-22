#!/usr/bin/env python3
"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


import json

import requests

from .errors import ThothError


class ThothQuery:
    """GraphQL query in Thoth

       Queries are specified in the QUERIES list of the API version, which
       specifies their fields and desired return value 'fields' must be a list
       of tuples (str, bool) where the string represents the attribute and the
       boolean represents whether the values should be enclosed with quotes
       and sanitised.
    """

    def __init__(self, query_name, parameters, queries, raw=False):
        """Returns new ThothQuery object

        mutation_name: Must match one of the keys found in MUTATIONS.

        mutation_data: Dictionary of mutation fields and their values.
        """
        self.QUERIES = queries
        self.query_name = query_name
        self.parameters = parameters
        self.param_str = self.prepare_parameters()
        self.fields_str = self.prepare_fields()
        self.request = self.prepare_request()
        self.raw = raw

    def prepare_request(self):
        """Format the query request string"""
        values = {
            "query_name": self.query_name,
            "parameters": "(" + self.param_str + ")" if self.param_str else '',
            "fields": "{" + self.fields_str + "}" if self.fields_str else ''
        }

        payload = """
            query {
                %(query_name)s%(parameters)s
                %(fields)s
            }
        """
        return payload % values

    def run(self, client):
        """Perform the GraphQL query and report any errors"""
        result = ""
        try:
            result = client.execute(self.request)
            serialised = json.loads(result)
            if "errors" in serialised:
                raise AssertionError
            if self.raw:
                return result
            return serialised["data"][self.query_name]
        except (KeyError, TypeError, ValueError, AssertionError,
                json.decoder.JSONDecodeError,
                requests.exceptions.RequestException):
            raise ThothError(self.request, result)

    def prepare_parameters(self):
        """Returns a string with all query parameters."""
        parameters = []
        for key, value in self.parameters.items():
            # note that we strip out extraneous quotation marks from parameters
            # because ORDER clauses, for instance, do not allow them

            parameters.append("{}: "
                              "{}, ".format(key, value))
        return ", ".join(parameters)

    def prepare_fields(self):
        """Returns a string with all query fields."""
        if self.query_name in self.QUERIES and \
                'fields' in self.QUERIES[self.query_name]:
            return "\n".join(self.QUERIES[self.query_name]["fields"])
        return ''

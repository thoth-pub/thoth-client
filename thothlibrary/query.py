#!/usr/bin/env python3
"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


import json
import urllib
from .errors import ThothError


class ThothQuery():
    """GraphQL query in Thoth

       Queries are specified in the QUERIES list, which specifies
       their fields and desired return value 'fields' must be a list of
       tuples (str, bool) where the string represents the attribute and the
       boolean represents whether the values should be enclosed with quotes
       and sanitised.
    """

    QUERIES = {
        "works": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
                "workType",
                "workStatus"
            ],
            "fields": [
                "workType",
                "workStatus",
                "fullTitle",
                "title",
                "subtitle",
                "reference",
                "edition",
                "imprintId",
                "doi",
                "publicationDate",
                "place",
                "width",
                "height",
                "pageCount",
                "pageBreakdown",
                "imageCount",
                "tableCount",
                "audioCount",
                "videoCount",
                "license",
                "copyrightHolder",
                "landingPage",
                "lccn",
                "oclc",
                "shortAbstract",
                "longAbstract",
                "generalNote",
                "toc",
                "coverUrl",
                "coverCaption"
            ]
        }
    }

    def __init__(self, query_name, parameters):
        """Returns new ThothMutation object with specified mutation data

        mutation_name: Must match one of the keys found in MUTATIONS.

        mutation_data: Dictionary of mutation fields and their values.
        """
        self.query_name = query_name
        self.parameters = parameters
        self.param_str = self.prepare_parameters()
        self.fields_str = self.prepare_fields()
        self.request = self.prepare_request()

    def prepare_request(self):
        """Format the query request string"""
        values = {
            "query_name": self.query_name,
            "parameters": self.param_str,
            "fields": self.fields_str
        }
        payload = """
            query {
                %(query_name)s(
                    %(parameters)s
                ) {
                    %(fields)s
                }
            }
        """
        return payload % values

    def run(self, client):
        """Perform the GraphQL query and report any errors"""
        result = ""
        try:
            result = client.execute(self.request)
            if "errors" in result:
                raise AssertionError
            return json.loads(result)["data"][self.query_name]
        except (KeyError, TypeError, ValueError, AssertionError,
                json.decoder.JSONDecodeError, urllib.error.HTTPError):
            raise ThothError(self.request, result)

    def prepare_parameters(self):
        """Returns a string with all query parameters."""
        parameters = []
        for key, value in self.parameters.items():
            parameters.append("{}: {}, ".format(key, json.dumps(value)))
        return ", ".join(parameters)

    def prepare_fields(self):
        """Returns a string with all query fields."""
        return "\n".join(self.QUERIES[self.query_name]["fields"])

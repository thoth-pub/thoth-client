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


class ThothMutation():
    """GraphQL mutation in Thoth

       Mutations are specified in the MUTATIONS list, which specifies
       their fields and desired return value 'fields' must be a list of
       tuples (str, bool) where the string represents the attribute and the
       boolean represents whether the values should be enclosed with quotes
       and sanitised.

       Each mutation must have a return_value. Normally this is the primary key
       of that object, but in some cases, when we don't need to use the return
       value, we simply specify any field that can be returned in that mutation
       (e.g. createContribution).
    """

    MUTATIONS = {
        "createPublisher": {
            "fields": [
                ("publisherName", True),
                ("publisherShortname", True),
                ("publisherUrl", True)
            ],
            "return_value": "publisherId"
        },
        "createImprint": {
            "fields": [
                ("publisherId", True),
                ("imprintName", True),
                ("imprintUrl", True)
            ],
            "return_value": "imprintId"
        },
        "createWork": {
            "fields": [
                ("workType", False),
                ("workStatus", False),
                ("fullTitle", True),
                ("title", True),
                ("subtitle", True),
                ("reference", True),
                ("edition", False),
                ("imprintId", True),
                ("doi", True),
                ("publicationDate", True),
                ("place", True),
                ("width", False),
                ("height", False),
                ("pageCount", False),
                ("pageBreakdown", True),
                ("imageCount", False),
                ("tableCount", False),
                ("audioCount", False),
                ("videoCount", False),
                ("license", True),
                ("copyrightHolder", True),
                ("landingPage", True),
                ("lccn", True),
                ("oclc", True),
                ("shortAbstract", True),
                ("longAbstract", True),
                ("generalNote", True),
                ("toc", True),
                ("coverUrl", True),
                ("coverCaption", True)
            ],
            "return_value": "workId"
        },
        "createPublication": {
            "fields": [
                ("publicationType", False),
                ("workId", True),
                ("isbn", True),
                ("publicationUrl", True)
            ],
            "return_value": "publicationId"
        },
        "createPrice": {
            "fields": [
                ("publicationId", True),
                ("currencyCode", False),
                ("unitPrice", False)
            ],
            "return_value": "priceId"
        },
        "createLanguage": {
            "fields": [
                ("workId", True),
                ("languageCode", False),
                ("languageRelation", False),
                ("mainLanguage", False)
            ],
            "return_value": "languageId"
        },
        "createSubject": {
            "fields": [
                ("workId", True),
                ("subjectType", False),
                ("subjectCode", True),
                ("subjectOrdinal", False)
            ],
            "return_value": "subjectId"
        },
        "createSeries": {
            "fields": [
                ("imprintId", True),
                ("seriesType", False),
                ("seriesName", True),
                ("issnPrint", True),
                ("issnDigital", True),
                ("seriesUrl", True)
            ],
            "return_value": "seriesId"
        },
        "createIssue": {
            "fields": [
                ("seriesId", True),
                ("workId", True),
                ("issueOrdinal", False)
            ],
            "return_value": "issueOrdinal"
        },
        "createContributor": {
            "fields": [
                ("firstName", True),
                ("lastName", True),
                ("fullName", True),
                ("orcid", True),
                ("website", True)
            ],
            "return_value": "contributorId"
        },
        "createContribution": {
            "fields": [
                ("workId", True),
                ("contributorId", True),
                ("contributionType", False),
                ("mainContribution", False),
                ("biography", True),
                ("institution", True),
                ("firstName", True),
                ("lastName", True),
                ("fullName", True)
            ],
            "return_value": "workId"
        }
    }

    def __init__(self, mutation_name, mutation_data):
        """Returns new ThothMutation object with specified mutation data

        mutation_name: Must match one of the keys found in MUTATIONS.

        mutation_data: Dictionary of mutation fields and their values.
        """
        self.mutation_name = mutation_name
        self.return_value = self.MUTATIONS[mutation_name]["return_value"]
        self.mutation_data = mutation_data
        self.data_str = self.generate_values()
        self.request = self.prepare_request()

    def prepare_request(self):
        """Format the mutation request string"""
        values = {
            "mutation_name": self.mutation_name,
            "data": self.data_str,
            "return_value": self.return_value
        }
        payload = """
            mutation {
                %(mutation_name)s(
                    data: {
                        %(data)s
                    }
                ) {
                    %(return_value)s
                }
            }
        """
        return payload % values

    def run(self, client):
        """Perform the GraphQL mutation and report any errors"""
        result = ""
        try:
            result = client.execute(self.request)
            if "errors" in result:
                raise AssertionError
            return json.loads(result)[
                "data"][self.mutation_name][self.return_value]
        except (KeyError, TypeError, ValueError, AssertionError,
                json.decoder.JSONDecodeError, urllib.error.HTTPError):
            raise ThothError(self.request, result)

    def generate_values(self):
        """Returns a set of mutation statements based on object attributes."""
        def sanitise(text):
            """Escape quotes and linebreaks"""
            tmp = text.replace("\n", "\\n")
            return tmp.replace('"', '''\\"''')
        values = []
        for key, enclose in self.MUTATIONS[self.mutation_name]["fields"]:
            value = self.mutation_data[key]
            if value is None or not str(value):
                continue
            if enclose:
                statement = "{}: \"{}\"".format(key, sanitise(value))
            else:
                statement = "{}: {}".format(key, value)
            values.append(statement)
        return "\n".join(values)

"""
REST client for Thoth's export API.

(c) Delta Q Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import requests

from .errors import ThothRESTError
from .rest_structures import StructureBuilder


class ThothRESTClient:
    """Client for Thoth's export API."""

    def __init__(self, endpoint="https://export.thoth.pub"):
        self.endpoint = endpoint

    def _api_request(self, endpoint_name, url_suffix, return_json=False,
                     return_raw=False):
        response = self._fetch(url_suffix)

        if return_json:
            return response.json()
        if return_raw:
            return response.text
        return self._build_structure(endpoint_name, response.json())

    def _build_structure(self, endpoint_name, data):
        builder = StructureBuilder(endpoint_name, data)
        return builder.create_structure()

    def _fetch(self, url_suffix):
        try:
            response = requests.get(self.endpoint + url_suffix)
            if response.status_code != 200:
                raise ThothRESTError(
                    "GET {0}{1}".format(self.endpoint, url_suffix),
                    response.status_code,
                )
            return response
        except requests.exceptions.RequestException as exc:
            raise ThothRESTError(
                "GET {0}{1}".format(self.endpoint, url_suffix),
                exc,
            )

    def formats(self, return_json=False):
        return self._api_request("formats", "/formats/", return_json)

    def format(self, identifier, return_json=False):
        return self._api_request(
            "format",
            "/formats/{0}".format(identifier),
            return_json,
        )

    def specifications(self, return_json=False):
        return self._api_request(
            "specifications",
            "/specifications/",
            return_json,
        )

    def specification(self, identifier, return_json=False):
        return self._api_request(
            "specification",
            "/specifications/{0}".format(identifier),
            return_json,
        )

    def platforms(self, return_json=False):
        return self._api_request("platforms", "/platforms/", return_json)

    def platform(self, identifier, return_json=False):
        return self._api_request(
            "platform",
            "/platforms/{0}".format(identifier),
            return_json,
        )

    def work(self, identifier, work_identifier):
        return self._api_request(
            "work",
            "/specifications/{0}/work/{1}".format(identifier, work_identifier),
            return_raw=True,
        )

    def works(self, identifier, publisher):
        return self._api_request(
            "publisher",
            "/specifications/{0}/publisher/{1}".format(identifier, publisher),
            return_raw=True,
        )

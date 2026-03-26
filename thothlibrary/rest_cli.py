"""
CLI for Thoth's export API.

(c) Delta Q Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import fire

from .rest import ThothRESTClient


class ThothRESTAPI:
    """Command line access to Thoth's export API."""

    def __init__(self):
        self.endpoint = "https://export.thoth.pub"

    def _client(self):
        return ThothRESTClient(endpoint=self.endpoint)

    def _override_endpoint(self, endpoint):
        if endpoint:
            self.endpoint = endpoint

    def formats(self, endpoint=None, return_json=False):
        self._override_endpoint(endpoint)
        print(self._client().formats(return_json=return_json))

    def format(self, identifier, endpoint=None, return_json=False):
        self._override_endpoint(endpoint)
        print(self._client().format(identifier, return_json=return_json))

    def specifications(self, endpoint=None, return_json=False):
        self._override_endpoint(endpoint)
        print(self._client().specifications(return_json=return_json))

    def specification(self, identifier, endpoint=None, return_json=False):
        self._override_endpoint(endpoint)
        print(self._client().specification(identifier,
                                           return_json=return_json))

    def platforms(self, endpoint=None, return_json=False):
        self._override_endpoint(endpoint)
        print(self._client().platforms(return_json=return_json))

    def platform(self, identifier, endpoint=None, return_json=False):
        self._override_endpoint(endpoint)
        print(self._client().platform(identifier, return_json=return_json))

    def work(self, identifier, work_identifier, endpoint=None):
        self._override_endpoint(endpoint)
        print(self._client().work(identifier, work_identifier))

    def works(self, identifier, publisher, endpoint=None):
        self._override_endpoint(endpoint)
        print(self._client().works(identifier, publisher))


if __name__ == "__main__":
    fire.Fire(ThothRESTAPI)

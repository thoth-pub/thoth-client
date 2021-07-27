"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import requests
from errors import ThothRESTError
import importlib


class ThothRESTClient:
    """A client for Thoth's REST API"""
    endpoint = 'https://export.thoth.pub'
    version = '042'

    def __init__(self, endpoint='https://export.thoth.pub', version='0.4.2'):
        """
        A REST client for Thoth
        @param endpoint: the endpoint of the server instance to use
        @param version: the version of the API to use
        """
        self.endpoint = endpoint
        self.version = version.replace('.', '')

    def formats(self, return_json=False):
        """
        Full list of metadata formats that can be output by Thoth
        @param return_json: whether to return JSON or an object (default)
        @return: an object or JSON
        """
        return self._api_request('formats', '/formats/', return_json)

    def format(self, identifier, return_json=False):
        """
        Find the details of a format that can be output by Thoth
        @param return_json: whether to return JSON or an object (default)
        @param identifier: the format ID to describe
        @return: an object or JSON
        """
        return self._api_request('format', '/formats/{0}'.format(identifier), return_json)

    def specifications(self, return_json=False):
        """
        Full list of metadata specifications that can be output by Thoth
        @param return_json: whether to return JSON or an object (default)
        @return: an object or JSON
        """
        return self._api_request('specifications', '/specifications/', return_json)

    def specification(self, identifier, return_json=False):
        """
        Find the details of a metadata specification that can be output by Thoth
        @param return_json: whether to return JSON or an object (default)
        @param identifier: the specification ID to describe
        @return: an object or JSON
        """
        return self._api_request('specification', '/specifications/{0}'.format(identifier), return_json)

    def platforms(self, return_json=False):
        """
        Full list of platforms supported by Thoth's outputs
        @param return_json: whether to return JSON or an object (default)
        @return: an object or JSON
        """
        return self._api_request('platforms', '/platforms/', return_json)

    def platform(self, identifier, return_json=False):
        """
        Find the details of a metadata specification that can be output by Thoth
        @param return_json: whether to return JSON or an object (default)
        @param identifier: the specification ID to describe
        @return: an object or JSON
        """
        return self._api_request('platform', '/platforms/{0}'.format(identifier), return_json)

    def work(self, identifier, work, return_json=False):
        """
        Obtain a metadata record that adheres to a particular specification for a given work
        @param return_json: whether to return JSON or an object (default)
        @param identifier: the specification ID
        @param identifier: the work ID
        @return: an object or JSON
        """
        return self._api_request('work', '/specifications/{0}/work/{1}'.format(identifier, work), False, True)

    def _api_request(self, endpoint_name, url_suffix, return_json=False, return_raw=False):
        """
        Makes a request to the API
        @param endpoint_name: the name of the endpoint
        @param url_suffix: the URL suffix
        @param return_json: whether to return raw JSON or an object (default)
        @param return_raw: whether to return the raw data returned
        @return: an object or JSON of the request
        """
        response = self._fetch(url_suffix)

        if return_json:
            return response.json()
        elif return_raw:
            return response.text
        else:
            return self._build_structure(endpoint_name, response.json())

    def _build_structure(self, endpoint_name, data):
        """
        Builds an object structure for an endpoint
        @param endpoint_name: the name of the endpoint
        @param data: the data
        @return: an object form of the output
        """
        structures = importlib.import_module('thoth-{0}.structures'.format(self.version))
        builder = structures.StructureBuilder(endpoint_name, data)
        return builder.create_structure()

    def _fetch(self, url_suffix):
        """
        Fetches JSON from the REST endpoint
        @param url_suffix: the URL suffix for the entry
        @return: a requests response object
        """
        try:
            resp = requests.get(self.endpoint + url_suffix)

            if resp.status_code != 200:
                raise ThothRESTError('GET {0}{1}'.format(self.endpoint, url_suffix), resp.status_code)

            return resp
        except requests.exceptions.RequestException as e:
            raise ThothRESTError('GET {0}{1}'.format(self.endpoint, url_suffix), e)

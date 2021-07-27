"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from client import ThothRESTClient


class ThothRESTClient042(ThothRESTClient):

    def __init__(self, input_class):
        # this is the magic dynamic generation part that wires up the methods
        input_class.formats = getattr(self, 'formats')
        input_class.format = getattr(self, 'format')
        input_class.specifications = getattr(self, 'specifications')
        input_class.specification = getattr(self, 'specification')
        input_class.platform = getattr(self, 'platform')
        input_class.platforms = getattr(self, 'platforms')
        input_class.work = getattr(self, 'work')
        input_class.works = getattr(self, 'works')

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
        @param identifier: the platform ID
        @return: an object or JSON
        """
        return self._api_request('platform', '/platforms/{0}'.format(identifier), return_json)

    def work(self, identifier, work_identifier):
        """
        Obtain a metadata record that adheres to a particular specification for a given work
        @param identifier: the specification ID
        @param work_identifier: the work ID
        @return: the metadata record
        """
        return self._api_request('work',
                                 '/specifications/{0}/work/{1}'.format(identifier, work_identifier), False, True)

    def works(self, identifier, publisher):
        """
        Obtain a metadata record that adheres to a particular specification for all of a given publisher's works
        @param identifier: the specification ID
        @param publisher: the publisher ID
        @return: an object or JSON
        """
        return self._api_request('publisher',
                                 '/specifications/{0}/publisher/{1}'.format(identifier, publisher), False, True)

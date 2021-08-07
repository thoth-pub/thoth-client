"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from thothlibrary.client import ThothClient


class ThothClient0_4_2(ThothClient):
    # the QUERIES field defines the fields that GraphQL will return
    # note: every query should contain the field "__typename" if auto-object
    # __str__ representation is to work
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
                "workId",
                "coverUrl",
                "coverCaption",
                "publications { isbn publicationType }",
                "contributions { fullName contributionType mainContribution contributionOrdinal }",
                "imprint { publisher { publisherName publisherId } }",
                "__typename"
            ]
        },

        "publications": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
                "publicationType",
            ],
            "fields": [
                "publicationId",
                "publicationType",
                "workId",
                "isbn",
                "publicationUrl",
                "createdAt",
                "updatedAt",
                "prices { currencyCode unitPrice __typename}",
                "work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } imprint { publisher { publisherName publisherId } } }",
                "__typename"
            ]
        },

        "workByDoi": {
            "parameters": [
                "doi"
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
                "coverCaption",
                "publications { isbn publicationType }",
                "contributions { fullName contributionType mainContribution contributionOrdinal }",
                "imprint { publisher { publisherName publisherId } }",
                "__typename"
            ]
        },

        "contributions": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
                "contributionType",
            ],
            "fields": [
                "contributionId",
                "contributionType",
                "mainContribution",
                "biography",
                "institution",
                "__typename",
                "firstName",
                "lastName",
                "fullName",
                "contributionOrdinal",
                "workId",
                "contributor {firstName lastName fullName orcid __typename website contributorId}"
            ]
        },

        "publishers": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
            ],
            "fields": [
                "imprints { imprintUrl imprintId imprintName}"
                "updatedAt",
                "createdAt",
                "publisherId",
                "publisherName",
                "publisherShortname",
                "publisherUrl",
                "__typename"
            ]
        },

        "publisher": {
            "parameters": [
                "publisherId",
            ],
            "fields": [
                "imprints { imprintUrl imprintId imprintName}"
                "updatedAt",
                "createdAt",
                "publisherId",
                "publisherName",
                "publisherShortname",
                "publisherUrl",
                "__typename"
            ]
        },

        "publisherCount": {
            "parameters": [
                "filter",
                "publishers",
            ],
        },

        "workCount": {
            "parameters": [
                "filter",
                "publishers",
                "workType",
                "workStatus",
            ],
        },

        "publicationCount": {
            "parameters": [
                "filter",
                "publishers",
                "publicationType"
            ],
        },

        "contributionCount": {
            "parameters": [
                "filter",
                "publishers",
                "contributionType"
            ],
        }
    }

    def __init__(self, input_class, thoth_endpoint="https://api.thoth.pub",
                 version="0.4.2"):
        """
        Creates an instance of Thoth 0.4.2 endpoints
        @param input_class: the ThothClient instance to be versioned
        """
        super().__init__(thoth_endpoint=thoth_endpoint,
                         version=version)

        # this is the magic dynamic generation part that wires up the methods
        input_class.works = getattr(self, 'works')
        input_class.work_by_doi = getattr(self, 'work_by_doi')
        input_class.publishers = getattr(self, 'publishers')
        input_class.publisher = getattr(self, 'publisher')
        input_class.publications = getattr(self, 'publications')
        input_class.contributions = getattr(self, 'contributions')
        input_class.publisher_count = getattr(self, 'publisher_count')
        input_class.contribution_count = getattr(self, 'contribution_count')
        input_class.work_count = getattr(self, 'work_count')
        input_class.publication_count = getattr(self, 'publication_count')
        input_class.QUERIES = getattr(self, 'QUERIES')

    def publications(self, limit: int = 100, offset: int = 0,
                     filter_str: str = "", order: str = None,
                     publishers: str = None, publication_type: str = None,
                     raw: bool = False):
        """
        Returns a publications list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param filter_str: a filter string to search
        @param publication_type: the work type (e.g. PAPERBACK)
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        if order is None:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publications", parameters, return_raw=raw)

    def contributions(self, limit: int = 100, offset: int = 0,
                      filter_str: str = "", order: str = None,
                      publishers: str = None, contribution_type: str = None,
                      raw: bool = False):
        """
        Returns a contributions list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param filter_str: a filter string to search
        @param contribution_type: the contribution type (e.g. AUTHOR)
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        if order is None:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'contributionType', contribution_type)

        return self._api_request("contributions", parameters, return_raw=raw)

    def works(self, limit: int = 100, offset: int = 0, filter_str: str = "",
              order: str = None, publishers: str = None, work_type: str = None,
              work_status: str = None, raw: bool = False):
        """
        Returns a works list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param filter_str: a filter string to search
        @param work_type: the work type (e.g. MONOGRAPH)
        @param work_status: the work status (e.g. ACTIVE)
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        if order is None:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'workType', work_type)
        self._dictionary_append(parameters, 'workStatus', work_status)

        return self._api_request("works", parameters, return_raw=raw)

    def work_by_doi(self, doi: str, raw: bool = False):
        """
        Returns a work by DOI
        @param doi: the DOI to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'doi': '"' + doi + '"'
        }

        return self._api_request("workByDoi", parameters, return_raw=raw)

    def publisher(self, publisher_id: str, raw: bool = False):
        """
        Returns a work by DOI
        @param publisher_id: the publisher
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'publisherId': '"' + publisher_id + '"'
        }

        return self._api_request("publisher", parameters, return_raw=raw)

    def publishers(self, limit: int = 100, offset: int = 0, order: str = None,
                   filter_str: str = "", publishers: str = None,
                   raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publishers", parameters, return_raw=raw)

    def publisher_count(self, filter_str: str = "", publishers: str = None,
                        raw: bool = False):
        """Construct and trigger a query to count publishers"""
        parameters = {}

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publisherCount", parameters, return_raw=raw)

    def work_count(self, filter_str: str = "", publishers: str = None,
                   work_type: str = None, work_status: str = None,
                   raw: bool = False):
        """Construct and trigger a query to count works"""
        parameters = {}

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'workType', work_type)
        self._dictionary_append(parameters, 'workStatus', work_status)

        return self._api_request("workCount", parameters, return_raw=raw)

    def contribution_count(self, filter_str: str = "", publishers: str = None,
                           contribution_type: str = None, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'contributionType',
                                contribution_type)

        return self._api_request("contributionCount", parameters, return_raw=raw)

    def publication_count(self, filter_str: str = "", publishers: str = None,
                          publication_type: str = None, raw: bool = False):
        """Construct and trigger a query to count publications"""
        parameters = {}

        self._dictionary_append(parameters, 'filter', filter_str)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publicationCount", parameters, return_raw=raw)

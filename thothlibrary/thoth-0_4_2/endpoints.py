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
                "publications { isbn publicationType __typename }",
                "contributions { fullName contributionType mainContribution contributionOrdinal __typename }",
                "imprint { __typename publisher { publisherName publisherId __typename } }",
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

        "publication": {
            "parameters": [
                "publicationId",
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

        "work": {
            "parameters": [
                "workId"
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
                "publications { isbn publicationType __typename }",
                "contributions { fullName contributionType mainContribution contributionOrdinal __typename }",
                "imprint { __typename publisher { publisherName publisherId __typename } }",
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
                "publications { isbn publicationType __typename }",
                "contributions { fullName contributionType mainContribution contributionOrdinal __typename }",
                "imprint { __typename publisher { publisherName publisherId __typename } }",
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
                "work { fullTitle }",
                "contributor {firstName lastName fullName orcid __typename website contributorId}"
            ]
        },

        "contribution": {
            "parameters": [
                "contributionId",
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
                "work { fullTitle }",
                "contributor {firstName lastName fullName orcid __typename website contributorId}"
            ]
        },

        "contributors": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
            ],
            "fields": [
                "contributorId",
                "firstName",
                "lastName",
                "fullName",
                "orcid",
                "__typename",
                "contributions { contributionId contributionType work { workId fullTitle} }"
            ]
        },

        "contributor": {
            "parameters": [
                "contributorId"
            ],
            "fields": [
                "contributorId",
                "firstName",
                "lastName",
                "fullName",
                "orcid",
                "__typename",
                "contributions { contributionId contributionType work { workId fullTitle} }"
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
                "imprints { imprintUrl imprintId imprintName __typename}"
                "updatedAt",
                "createdAt",
                "publisherId",
                "publisherName",
                "publisherShortname",
                "publisherUrl",
                "__typename"
            ]
        },

        "serieses": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
                "seriesType"
            ],
            "fields": [
                "seriesId",
                "seriesType",
                "seriesName",
                "updatedAt",
                "createdAt",
                "imprintId",
                "imprint { __typename publisher { publisherName publisherId __typename } }",
                "issues { issueId work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } } }",
                "__typename"
            ]
        },

        "series": {
            "parameters": [
                "seriesId"
            ],
            "fields": [
                "seriesId",
                "seriesType",
                "seriesName",
                "updatedAt",
                "createdAt",
                "imprintId",
                "imprint { __typename publisher { publisherName publisherId __typename } }",
                "issues { issueId work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } } }",
                "__typename"
            ]
        },

        "issue": {
            "parameters": [
                "issueId",
            ],
            "fields": [
                "issueId",
                "seriesId",
                "issueOrdinal",
                "updatedAt",
                "createdAt",
                "series { seriesId seriesType seriesName imprintId imprint { __typename publisher { publisherName publisherId __typename } }}",
                "work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } }"
                "__typename"
            ]
        },

        "issues": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
            ],
            "fields": [
                "issueId",
                "seriesId",
                "issueOrdinal",
                "updatedAt",
                "createdAt",
                "series { seriesId seriesType seriesName imprintId imprint { __typename publisher { publisherName publisherId __typename } }}",
                "work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } }"
                "__typename"
            ]
        },

        "imprints": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
            ],
            "fields": [
                "imprintUrl",
                "imprintId",
                "imprintName",
                "updatedAt",
                "createdAt",
                "publisherId",
                "publisher { publisherName publisherId }",
                "works { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } }"
                "__typename"
            ]
        },

        "language": {
            "parameters": [
                "languageId",
            ],
            "fields": [
                "languageId",
                "workId",
                "languageCode",
                "languageRelation",
                "createdAt",
                "mainLanguage",
                "work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } }"
                "__typename"
            ]
        },

        "languages": {
            "parameters": [
                "limit",
                "offset",
                "filter",
                "order",
                "publishers",
                "languageCode",
                "languageRelation"
            ],
            "fields": [
                "languageId",
                "workId",
                "languageCode",
                "languageRelation",
                "createdAt",
                "mainLanguage",
                "work { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } }"
                "__typename"
            ]
        },

        "imprint": {
            "parameters": [
                "imprintId",
            ],
            "fields": [
                "imprintUrl",
                "imprintId",
                "imprintName",
                "updatedAt",
                "createdAt",
                "publisherId",
                "publisher { publisherName publisherId }",
                "works { workId fullTitle doi publicationDate place contributions { fullName contributionType mainContribution contributionOrdinal } }"
                "__typename"
            ]
        },

        "publisher": {
            "parameters": [
                "publisherId",
            ],
            "fields": [
                "imprints { imprintUrl imprintId imprintName __typename}"
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

        "imprintCount": {
            "parameters": [
                "filter",
                "publishers",
            ],
        },

        "contributorCount": {
            "parameters": [
                "filter",
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
        },

        "issuesCount": None,

        "seriesCount": {
            "parameters": [
                "filter",
                "publishers",
                "seriesType"
            ],
        }
    }

    def __init__(self, thoth_endpoint="https://api.thoth.pub", version="0.4.2"):
        """
        Creates an instance of Thoth 0.4.2 endpoints
        @param input_class: the ThothClient instance to be versioned
        """

        # this list should specify all API endpoints by method name in this
        # class. Note, it should always, also, contain the QUERIES list
        self.endpoints = ['works', 'work_by_doi', 'work_by_id',
                          'publishers', 'publisher', 'publications',
                          'contributions', 'contribution', 'publisher_count',
                          'contribution_count', 'work_count',
                          'publication_count', 'publication', 'imprints',
                          'imprint', 'imprint_count', 'contributors',
                          'contributor', 'contributor_count', 'serieses',
                          'series', 'series_count', 'issues',
                          'issue', 'issue_count', 'languages', 'language',
                          'QUERIES']

        super().__init__(thoth_endpoint=thoth_endpoint,
                         version=version)

    def contributor(self, contributor_id: str, raw: bool = False):
        """
        Returns a contributor by ID
        @param contributor_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'contributorId': '"' + contributor_id + '"'
        }

        return self._api_request("contributor", parameters, return_raw=raw)

    def language(self, language_id: str, raw: bool = False):
        """
        Returns a series by ID
        @param language_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'languageId': '"' + language_id + '"'
        }

        return self._api_request("language", parameters, return_raw=raw)

    def series(self, series_id: str, raw: bool = False):
        """
        Returns a series by ID
        @param series_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'seriesId': '"' + series_id + '"'
        }

        return self._api_request("series", parameters, return_raw=raw)

    def publication(self, publication_id: str, raw: bool = False):
        """
        Returns a publication by ID
        @param publication_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'publicationId': '"' + publication_id + '"'
        }

        return self._api_request("publication", parameters, return_raw=raw)

    def publications(self, limit: int = 100, offset: int = 0,
                     filter: str = "", order: str = None,
                     publishers: str = None, publication_type: str = None,
                     raw: bool = False):
        """
        Returns a publications list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param filter: a filter string to search
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

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publications", parameters, return_raw=raw)

    def contributions(self, limit: int = 100, offset: int = 0,
                      order: str = None, publishers: str = None,
                      contribution_type: str = None, raw: bool = False):
        """
        Returns a contributions list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
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

        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'contributionType',
                                contribution_type)

        return self._api_request("contributions", parameters, return_raw=raw)

    def contributors(self, limit: int = 100, offset: int = 0,
                     filter: str = "", order: str = None,
                     raw: bool = False):
        """
        Returns a contributions list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param filter: a filter string to search
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        if order is None:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)

        return self._api_request("contributors", parameters, return_raw=raw)

    def works(self, limit: int = 100, offset: int = 0, filter: str = "",
              order: str = None, publishers: str = None, work_type: str = None,
              work_status: str = None, raw: bool = False):
        """
        Returns a works list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param filter: a filter string to search
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

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
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

    def work_by_id(self, work_id: str, raw: bool = False):
        """
        Returns a work by ID
        @param work_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'workId': '"' + work_id + '"'
        }

        return self._api_request("work", parameters, return_raw=raw)

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

    def contribution(self, contribution_id: str, raw: bool = False):
        """
        Returns a contribution by ID
        @param contribution_id: the contribution ID
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'contributionId': '"' + contribution_id + '"'
        }

        return self._api_request("contribution", parameters, return_raw=raw)

    def imprint(self, imprint_id: str, raw: bool = False):
        """
        Returns a work by DOI
        @param imprint_id: the imprint
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'imprintId': '"' + imprint_id + '"'
        }

        return self._api_request("imprint", parameters, return_raw=raw)

    def issue(self, issue_id: str, raw: bool = False):
        """
        Returns an issue by ID
        @param issue_id: the imprint
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'issueId': '"' + issue_id + '"'
        }

        return self._api_request("issue", parameters, return_raw=raw)

    def publishers(self, limit: int = 100, offset: int = 0, order: str = None,
                   filter: str = "", publishers: str = None,
                   raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publishers", parameters, return_raw=raw)

    def serieses(self, limit: int = 100, offset: int = 0, order: str = None,
                 filter: str = "", publishers: str = None,
                 series_type: str = "", raw: bool = False):
        """Construct and trigger a query to obtain all serieses"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'seriesType', series_type)

        return self._api_request("serieses", parameters, return_raw=raw)

    def imprints(self, limit: int = 100, offset: int = 0, order: str = None,
                 filter: str = "", publishers: str = None,
                 raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("imprints", parameters, return_raw=raw)

    def languages(self, limit: int = 100, offset: int = 0, order: str = None,
                  filter: str = "", publishers: str = None, raw: bool = False,
                  language_code: str = "", language_relation: str = ""):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'languageCode', language_code)
        self._dictionary_append(parameters, 'languageRelation',
                                language_relation)

        return self._api_request("languages", parameters, return_raw=raw)

    def issues(self, limit: int = 100, offset: int = 0, order: str = None,
               filter: str = "", publishers: str = None, raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("issues", parameters, return_raw=raw)

    def publisher_count(self, filter: str = "", publishers: str = None,
                        raw: bool = False):
        """Construct and trigger a query to count publishers"""
        parameters = {}

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publisherCount", parameters, return_raw=raw)

    def imprint_count(self, filter: str = "", publishers: str = None,
                      raw: bool = False):
        """Construct and trigger a query to count publishers"""
        parameters = {}

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("imprintCount", parameters, return_raw=raw)

    def work_count(self, filter: str = "", publishers: str = None,
                   work_type: str = None, work_status: str = None,
                   raw: bool = False):
        """Construct and trigger a query to count works"""
        parameters = {}

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'workType', work_type)
        self._dictionary_append(parameters, 'workStatus', work_status)

        return self._api_request("workCount", parameters, return_raw=raw)

    def series_count(self, filter: str = "", publishers: str = None,
                     series_type: str = None, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'seriesType',
                                series_type)

        return self._api_request("seriesCount", parameters, return_raw=raw)

    def contribution_count(self, filter: str = "", publishers: str = None,
                           contribution_type: str = None, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'contributionType',
                                contribution_type)

        return self._api_request("contributionCount", parameters,
                                 return_raw=raw)

    def publication_count(self, filter: str = "", publishers: str = None,
                          publication_type: str = None, raw: bool = False):
        """Construct and trigger a query to count publications"""
        parameters = {}

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publicationCount", parameters,
                                 return_raw=raw)

    def contributor_count(self, filter: str = "", raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if filter and not filter.startswith('"'):
            filter = '"{0}"'.format(filter)

        self._dictionary_append(parameters, 'filter', filter)

        return self._api_request("contributorCount", parameters,
                                 return_raw=raw)

    def issue_count(self, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        return self._api_request("issueCount", parameters,
                                 return_raw=raw)
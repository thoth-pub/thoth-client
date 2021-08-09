"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json

from thothlibrary.client import ThothClient


class ThothClient0_4_2(ThothClient):
    """
    The client for Thoth 0.4.2
    """

    def __init__(self, thoth_endpoint="https://api.thoth.pub", version="0.4.2"):
        """
        Creates an instance of Thoth 0.4.2 endpoints
        @param input_class: the ThothClient instance to be versioned
        """

        # the QUERIES field defines the fields that GraphQL will return
        # note: every query should contain the field "__typename" if auto-object
        # __str__ representation is to work. These are stored in the
        # fixtures/QUERIES file
        path = 'thothlibrary/thoth-{0}/fixtures/QUERIES'
        with open(path.format(version.replace('.', '_')), 'r') as query_file:
            self.QUERIES = json.loads(query_file.read())

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
                          'language_count', 'prices', 'price', 'price_count',
                          'subjects', 'subject', 'subject_count', 'funders',
                          'funder', 'funder_count', 'fundings', 'funding',
                          'funding_count', 'QUERIES']

        super().__init__(thoth_endpoint=thoth_endpoint,
                         version=version)

    def funding(self, funding_id: str, raw: bool = False):
        """
        Returns a funding by ID
        @param funding_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'fundingId': '"' + funding_id + '"'
        }

        return self._api_request("funding", parameters, return_raw=raw)

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

    def funder(self, funder_id: str, raw: bool = False):
        """
        Returns a funder by ID
        @param funder_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'funderId': '"' + funder_id + '"'
        }

        return self._api_request("funder", parameters, return_raw=raw)

    def subject(self, subject_id: str, raw: bool = False):
        """
        Returns a subject by ID
        @param subject_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'subjectId': '"' + subject_id + '"'
        }

        return self._api_request("subject", parameters, return_raw=raw)

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

    def price(self, price_id: str, raw: bool = False):
        """
        Returns a price by ID
        @param price_id: the ID to fetch
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'priceId': '"' + price_id + '"'
        }

        return self._api_request("price", parameters, return_raw=raw)

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

    def fundings(self, limit: int = 100, offset: int = 0, order: str = None,
                 publishers: str = None, raw: bool = False):
        """
        Returns a fundings list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
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

        return self._api_request("fundings", parameters, return_raw=raw)

    def prices(self, limit: int = 100, offset: int = 0, order: str = None,
               publishers: str = None, currency_code: str = None,
               raw: bool = False):
        """
        Returns a price list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param currency_code: the currency code (e.g. GBP)
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
        self._dictionary_append(parameters, 'currencyCode', currency_code)

        return self._api_request("prices", parameters, return_raw=raw)

    def publications(self, limit: int = 100, offset: int = 0,
                     search: str = "", order: str = None,
                     publishers: str = None, publication_type: str = None,
                     raw: bool = False):
        """
        Returns a publications list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param search: a filter string to search
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

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
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
                     search: str = "", order: str = None,
                     raw: bool = False):
        """
        Returns a contributions list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param search: a filter string to search
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        if order is None:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)

        return self._api_request("contributors", parameters, return_raw=raw)

    def works(self, limit: int = 100, offset: int = 0, search: str = "",
              order: str = None, publishers: str = None, work_type: str = None,
              work_status: str = None, raw: bool = False):
        """
        Returns a works list
        @param limit: the maximum number of results to return (default: 100)
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results (default: 0)
        @param publishers: a list of publishers to limit by
        @param search: a filter string to search
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

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
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
                   search: str = "", publishers: str = None,
                   raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publishers", parameters, return_raw=raw)

    def serieses(self, limit: int = 100, offset: int = 0, order: str = None,
                 search: str = "", publishers: str = None,
                 series_type: str = "", raw: bool = False):
        """Construct and trigger a query to obtain all serieses"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'seriesType', series_type)

        return self._api_request("serieses", parameters, return_raw=raw)

    def imprints(self, limit: int = 100, offset: int = 0, order: str = None,
                 search: str = "", publishers: str = None,
                 raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("imprints", parameters, return_raw=raw)

    def languages(self, limit: int = 100, offset: int = 0, order: str = None,
                  search: str = "", publishers: str = None, raw: bool = False,
                  language_code: str = "", language_relation: str = ""):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'languageCode', language_code)
        self._dictionary_append(parameters, 'languageRelation',
                                language_relation)

        return self._api_request("languages", parameters, return_raw=raw)

    def funders(self, limit: int = 100, offset: int = 0, order: str = None,
                search: str = "", raw: bool = False):
        """Construct and trigger a query to obtain all funders"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)

        return self._api_request("funders", parameters, return_raw=raw)

    def subjects(self, limit: int = 100, offset: int = 0, order: str = None,
                 search: str = "", publishers: str = None, raw: bool = False,
                 subject_type: str = ""):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'subjectType', subject_type)

        return self._api_request("subjects", parameters, return_raw=raw)

    def issues(self, limit: int = 100, offset: int = 0, order: str = None,
               search: str = "", publishers: str = None, raw: bool = False):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("issues", parameters, return_raw=raw)

    def publisher_count(self, search: str = "", publishers: str = None,
                        raw: bool = False):
        """Construct and trigger a query to count publishers"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publisherCount", parameters, return_raw=raw)

    def price_count(self, currency_code: str = None, raw: bool = False):
        """Construct and trigger a query to count publishers"""
        parameters = {}

        self._dictionary_append(parameters, 'currencyCode', currency_code)

        return self._api_request("priceCount", parameters, return_raw=raw)

    def imprint_count(self, search: str = "", publishers: str = None,
                      raw: bool = False):
        """Construct and trigger a query to count publishers"""
        parameters = {}

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("imprintCount", parameters, return_raw=raw)

    def work_count(self, search: str = "", publishers: str = None,
                   work_type: str = None, work_status: str = None,
                   raw: bool = False):
        """Construct and trigger a query to count works"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'workType', work_type)
        self._dictionary_append(parameters, 'workStatus', work_status)

        return self._api_request("workCount", parameters, return_raw=raw)

    def series_count(self, search: str = "", publishers: str = None,
                     series_type: str = None, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'seriesType',
                                series_type)

        return self._api_request("seriesCount", parameters, return_raw=raw)

    def contribution_count(self, search: str = "", publishers: str = None,
                           contribution_type: str = None, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'contributionType',
                                contribution_type)

        return self._api_request("contributionCount", parameters,
                                 return_raw=raw)

    def publication_count(self, search: str = "", publishers: str = None,
                          publication_type: str = None, raw: bool = False):
        """Construct and trigger a query to count publications"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publicationCount", parameters,
                                 return_raw=raw)

    def funder_count(self, search: str = "", raw: bool = False):
        """Construct and trigger a query to count publications"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)

        return self._api_request("funderCount", parameters, return_raw=raw)

    def contributor_count(self, search: str = "", raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)

        return self._api_request("contributorCount", parameters,
                                 return_raw=raw)

    def language_count(self, language_code: str = "",
                       language_relation: str = "", raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        self._dictionary_append(parameters, 'languageCode', language_code)
        self._dictionary_append(parameters, 'languageRelation',
                                language_relation)

        return self._api_request("languageCount", parameters, return_raw=raw)

    def subject_count(self, subject_type: str = "", search: str = "",
                      raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        # there is a bug in this version of Thoth. Filter is REQUIRED.
        if not filter:
            filter = '""'

        self._dictionary_append(parameters, 'subjectType', subject_type)
        self._dictionary_append(parameters, 'filter', search)

        return self._api_request("subjectCount", parameters, return_raw=raw)

    def issue_count(self, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        return self._api_request("issueCount", parameters,
                                 return_raw=raw)

    def funding_count(self, raw: bool = False):
        """Construct and trigger a query to count contribution count"""
        parameters = {}

        return self._api_request("fundingCount", parameters, return_raw=raw)

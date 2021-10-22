"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json
import os
import pathlib

import thothlibrary
from thothlibrary.client import ThothClient


class ThothClient0_4_2(ThothClient):
    """
    The client for Thoth 0.4.2
    """

    def __new__(cls, *args, **kwargs):
        return super(thothlibrary.ThothClient, ThothClient0_4_2).__new__(cls)

    def __init__(self, thoth_endpoint="https://api.thoth.pub", version="0.4.2"):
        """
        Creates an instance of Thoth 0.4.2 endpoints
        @param thoth_endpoint: the Thoth API instance endpoint
        @param version: the version of the Thoth API to use
        """
        if hasattr(self, 'client'):
            return

        # the QUERIES field defines the fields that GraphQL will return
        # note: every query should contain the field "__typename" if auto-object
        # __str__ representation is to work. These are stored in the
        # fixtures/QUERIES file
        script_dir = pathlib.Path(__file__).parent.resolve()
        path = os.path.join(script_dir, 'fixtures', 'QUERIES')

        with open(path, 'r') as query_file:
            self.QUERIES = json.loads(query_file.read())

        super().__init__(thoth_endpoint=thoth_endpoint, version=version)

    @staticmethod
    def _order_limit_filter_offset_setup(order, limit, search, offset):
        """
        The default setup for this version. Many methods use order, limit,
        filter, and offset as parameters, so this de-duplicates that code.
        @param order: the order
        @param limit: the limit
        @param search: the search
        @param offset: the offset
        @return: a parameters dictionary
        """
        if not order:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        ThothClient._dictionary_append(parameters, 'filter', search)
        ThothClient._dictionary_append(parameters, 'order', order)

        return parameters

    def contribution(self, contribution_id: str, raw: bool = False):
        """
        Returns a contribution by ID
        @param contribution_id: the contribution ID
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'contributionId': '"' + contribution_id + '"'
        }

        return self._api_request("contribution", parameters, return_raw=raw)

    def contributions(self, limit: int = 100, offset: int = 0,
                      order: str = None, publishers: str = None,
                      contribution_type: str = None, raw: bool = False):
        """
        Returns a contributions list
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
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

    def contribution_count(self, search: str = "", publishers: str = None,
                           contribution_type: str = None, raw: bool = False):
        """
        Returns a count of contributions
        @param search: a search string
        @param publishers: a list of publishers
        @param contribution_type: a contribution type (e.g. AUTHOR)
        @param raw: whether to return a raw result
        @return: a count of contributions
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'contributionType',
                                contribution_type)

        return self._api_request("contributionCount", parameters,
                                 return_raw=raw)

    def contributor(self, contributor_id: str, raw: bool = False):
        """
        Returns a contributor by ID
        @param contributor_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'contributorId': '"' + contributor_id + '"'
        }

        return self._api_request("contributor", parameters, return_raw=raw)

    def contributors(self, limit: int = 100, offset: int = 0,
                     search: str = "", order: str = None,
                     raw: bool = False):
        """
        Returns contributors
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
        @param search: a filter string to search
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)

        return self._api_request("contributors", parameters, return_raw=raw)

    def contributor_count(self, search: str = "", raw: bool = False):
        """
        Return a count of contributors
        @param search: a search string
        @param raw: whether to return the raw result
        @return: a count of contributors
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)

        return self._api_request("contributorCount", parameters,
                                 return_raw=raw)

    def funder(self, funder_id: str, raw: bool = False):
        """
        Returns a funder by ID
        @param funder_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'funderId': '"' + funder_id + '"'
        }

        return self._api_request("funder", parameters, return_raw=raw)

    def funders(self, limit: int = 100, offset: int = 0, order: str = None,
                search: str = "", raw: bool = False):
        """
        Return funders
        @param limit: the limit on the number of results
        @param offset: the offset from which to start
        @param order: the order of results
        @param search: a search string
        @param raw: whether to return raw result
        @return: an object or raw result
        """

        parameters = {
            "limit": limit,
            "offset": offset,
        }

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'order', order)

        return self._api_request("funders", parameters, return_raw=raw)

    def funder_count(self, search: str = "", raw: bool = False):
        """
        A count of funders
        @param search: a search string
        @param raw: whether to return raw result
        @return: a count of funders
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)

        return self._api_request("funderCount", parameters, return_raw=raw)

    def funding(self, funding_id: str, raw: bool = False):
        """
        Returns a funding by ID
        @param funding_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'fundingId': '"' + funding_id + '"'
        }

        return self._api_request("funding", parameters, return_raw=raw)

    def fundings(self, limit: int = 100, offset: int = 0, order: str = None,
                 publishers: str = None, raw: bool = False):
        """
        Returns a fundings list
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
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

    def funding_count(self, raw: bool = False):
        """
        A count of fundings
        @param raw: whether to return a raw result
        @return: a count of fundings
        """
        parameters = {}

        return self._api_request("fundingCount", parameters, return_raw=raw)

    def imprint(self, imprint_id: str, raw: bool = False):
        """
        Return an imprint
        @param imprint_id: the imprint
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'imprintId': '"' + imprint_id + '"'
        }

        return self._api_request("imprint", parameters, return_raw=raw)

    def imprints(self, limit: int = 100, offset: int = 0, order: str = None,
                 search: str = "", publishers: str = None,
                 raw: bool = False):
        """
        Return imprints
        @param limit: the limit on the number of results returned
        @param offset: the offset from which to begin
        @param order: the order in which to present results
        @param search: a search string
        @param publishers: a list of publishers by which to limit the query
        @param raw: whether to return a raw result
        @return: an object or raw result
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("imprints", parameters, return_raw=raw)

    def imprint_count(self, search: str = "", publishers: str = None,
                      raw: bool = False):
        """
        A count of imprints
        @param search: a search string
        @param publishers: a list of publishers by which to limit the result
        @param raw: whether to return a raw result
        @return: a count of imprints
        """
        parameters = {}

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("imprintCount", parameters, return_raw=raw)

    def issue(self, issue_id: str, raw: bool = False):
        """
        Returns an issue by ID
        @param issue_id: the issue
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'issueId': '"' + issue_id + '"'
        }

        return self._api_request("issue", parameters, return_raw=raw)

    def issues(self, limit: int = 100, offset: int = 0, order: str = None,
               search: str = "", publishers: str = None, raw: bool = False):
        """
        Return issues
        @param limit: the limit on the number of results to return
        @param offset: the offset from which to begin
        @param order: the order in which to return results
        @param search: a search string
        @param publishers: a list of publishers by which to limit results
        @param raw: whether to return a raw response
        @return: an object or raw response
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("issues", parameters, return_raw=raw)

    def issue_count(self, raw: bool = False):
        """
        A count of issues
        @param raw: whether to return a raw result
        @return: a count of issues
        """
        parameters = {}

        return self._api_request("issueCount", parameters,
                                 return_raw=raw)

    def language(self, language_id: str, raw: bool = False):
        """
        Returns a language by ID
        @param language_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'languageId': '"' + language_id + '"'
        }

        return self._api_request("language", parameters, return_raw=raw)

    def languages(self, limit: int = 100, offset: int = 0, order: str = None,
                  search: str = "", publishers: str = None, raw: bool = False,
                  language_code: str = "", language_relation: str = ""):
        """
        Return languages
        @param limit: the limit on the number of results to return
        @param offset: the offset from which to begin
        @param order: the order in which to return results
        @param search: a search string
        @param publishers: a list of publishers by which to limit the result
        @param raw: whether to return a raw result
        @param language_code: the language code to query
        @param language_relation: the language relation to query (e.g. ORIGINAL)
        @return: an object or raw result
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'languageCode', language_code)
        self._dictionary_append(parameters, 'languageRelation',
                                language_relation)

        return self._api_request("languages", parameters, return_raw=raw)

    def language_count(self, language_code: str = "",
                       language_relation: str = "", raw: bool = False):
        """
        A count of languages
        @param language_code: a language code (e.g. CHI)
        @param language_relation: a language relation (e.g. ORIGINAL)
        @param raw: whether to return a raw result
        @return: a count of languages
        """
        parameters = {}

        self._dictionary_append(parameters, 'languageCode', language_code)
        self._dictionary_append(parameters, 'languageRelation',
                                language_relation)

        return self._api_request("languageCount", parameters, return_raw=raw)

    def price(self, price_id: str, raw: bool = False):
        """
        Returns a price by ID
        @param price_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'priceId': '"' + price_id + '"'
        }

        return self._api_request("price", parameters, return_raw=raw)

    def prices(self, limit: int = 100, offset: int = 0, order: str = None,
               publishers: str = None, currency_code: str = None,
               raw: bool = False):
        """
        Returns prices
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
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

    def price_count(self, currency_code: str = None, raw: bool = False):
        """
        A count of prices
        @param currency_code: a currency code (e.g. GBP)
        @param raw: whether to return a raw result
        @return: a count of prices
        """
        parameters = {}

        self._dictionary_append(parameters, 'currencyCode', currency_code)

        return self._api_request("priceCount", parameters, return_raw=raw)

    def publication(self, publication_id: str, raw: bool = False):
        """
        Returns a publication by ID
        @param publication_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'publicationId': '"' + publication_id + '"'
        }

        return self._api_request("publication", parameters, return_raw=raw)

    def publications(self, limit: int = 100, offset: int = 0,
                     search: str = "", order: str = None,
                     publishers: str = None, publication_type: str = None,
                     raw: bool = False):
        """
        Returns publications
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
        @param publishers: a list of publishers to limit by
        @param search: a filter string to search
        @param publication_type: the work type (e.g. PAPERBACK)
        @param raw: whether to return a python object or the raw server result
        @return: either an object (default) or raw server response
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publications", parameters, return_raw=raw)

    def publication_count(self, search: str = "", publishers: str = None,
                          publication_type: str = None, raw: bool = False):
        """
        A count of publications
        @param search: a search string
        @param publishers: a list of publishers by which to limit the result
        @param publication_type: the publication type (e.g. PAPERBACK)
        @param raw: whether to return a raw result
        @return: a count of publications
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'publicationType', publication_type)

        return self._api_request("publicationCount", parameters,
                                 return_raw=raw)

    def publisher(self, publisher_id: str, raw: bool = False):
        """
        Returns a publisher by ID
        @param publisher_id: the publisher
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'publisherId': '"' + publisher_id + '"'
        }

        return self._api_request("publisher", parameters, return_raw=raw)

    def publishers(self, limit: int = 100, offset: int = 0, order: str = None,
                   search: str = "", publishers: str = None,
                   raw: bool = False):
        """
        Return publishers
        @param limit: the limit on the number of results
        @param offset: the offset from which to begin
        @param order: the order for the returned results
        @param search: a search string
        @param publishers: a list of publishers by which to limit the results
        @param raw: whether to return a raw result
        @return: an object or raw result
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publishers", parameters, return_raw=raw)

    def publisher_count(self, search: str = "", publishers: str = None,
                        raw: bool = False):
        """
        Return a count of publishers
        @param search: a search string
        @param publishers: a list of publishers by which to limit the result
        @param raw: whether to return a raw result
        @return: a count of publishers
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)

        return self._api_request("publisherCount", parameters, return_raw=raw)

    def series(self, series_id: str, raw: bool = False):
        """
        Returns a series by ID
        @param series_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'seriesId': '"' + series_id + '"'
        }

        return self._api_request("series", parameters, return_raw=raw)

    def serieses(self, limit: int = 100, offset: int = 0, order: str = None,
                 search: str = "", publishers: str = None,
                 series_type: str = "", raw: bool = False):
        """
        Return serieses
        @param limit: the limit on the number of results to retrieve
        @param offset: the offset from which to start
        @param order: the order in which to present the results
        @param search: a search string
        @param publishers: a list of publishers by which to limit results
        @param series_type: the series type (e.g. BOOK_SERIES)
        @param raw: whether to return a raw result
        @return: an object or raw result
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'seriesType', series_type)

        return self._api_request("serieses", parameters, return_raw=raw)

    def series_count(self, search: str = "", publishers: str = None,
                     series_type: str = None, raw: bool = False):
        """
        Return a count of serieses
        @param search: a search string
        @param publishers: a list of publishers by which to limit the results
        @param series_type: the type of series (e.g. BOOK_SERIES)
        @param raw: whether to return a raw result
        @return: a count of serieses
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'seriesType',
                                series_type)

        return self._api_request("seriesCount", parameters, return_raw=raw)

    def subject(self, subject_id: str, raw: bool = False):
        """
        Returns a subject by ID
        @param subject_id: the ID to fetch
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'subjectId': '"' + subject_id + '"'
        }

        return self._api_request("subject", parameters, return_raw=raw)

    def subjects(self, limit: int = 100, offset: int = 0, order: str = None,
                 search: str = "", publishers: str = None, raw: bool = False,
                 subject_type: str = ""):
        """
        Return subjects
        @param limit: a limit on the number of results
        @param offset: the offset from which to retrieve results
        @param order: the order in which to present results
        @param search: a search string
        @param publishers: a list of publishers
        @param raw: whether to return a raw result
        @param subject_type: the subject type (e.g. BIC)
        @return: subjects
        """
        parameters = self._order_limit_filter_offset_setup(order=order,
                                                           search=search,
                                                           limit=limit,
                                                           offset=offset)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'subjectType', subject_type)

        return self._api_request("subjects", parameters, return_raw=raw)

    def subject_count(self, subject_type: str = "", search: str = "",
                      raw: bool = False):
        """
        A count of subjects
        @param subject_type: the type of subject
        @param search: a search string
        @param raw: whether to return a raw result
        @return: a count of subjects
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        # there is a bug in this version of Thoth. Filter is REQUIRED.
        if not search:
            search = '""'

        self._dictionary_append(parameters, 'subjectType', subject_type)
        self._dictionary_append(parameters, 'filter', search)

        return self._api_request("subjectCount", parameters, return_raw=raw)

    def works(self, limit: int = 100, offset: int = 0, search: str = "",
              order: str = None, publishers: str = None, work_type: str = None,
              work_status: str = None, raw: bool = False):
        """
        Returns works
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
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
        @param raw: whether to return a python object or the raw result
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
        @param raw: whether to return a python object or the raw result
        @return: either an object (default) or raw server response
        """
        parameters = {
            'workId': '"' + work_id + '"'
        }

        return self._api_request("work", parameters, return_raw=raw)

    def work_count(self, search: str = "", publishers: str = None,
                   work_type: str = None, work_status: str = None,
                   raw: bool = False):
        """
        A count of works
        @param search: a search string
        @param publishers: a list of publishers by which to limit results
        @param work_type: the work type (e.g. MONOGRAPH)
        @param work_status: the work status (e.g. ACTIVE)
        @param raw: whether to return a raw result
        @return: a count of works
        """
        parameters = {}

        if search and not search.startswith('"'):
            search = '"{0}"'.format(search)

        self._dictionary_append(parameters, 'filter', search)
        self._dictionary_append(parameters, 'publishers', publishers)
        self._dictionary_append(parameters, 'workType', work_type)
        self._dictionary_append(parameters, 'workStatus', work_status)

        return self._api_request("workCount", parameters, return_raw=raw)

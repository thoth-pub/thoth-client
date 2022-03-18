"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json

import fire
from graphqlclient import GraphQLClient
from os import getenv

import thothlibrary


def _raw_parse(value):
    """
    This function overrides fire's default argument parsing using decorators.
    We need this because, otherwise, fire converts '{field: x}' to a
    dictionary object, which messes with GraphQL parameters.
    :param value: the input value
    :return: the parsed value
    """
    return value


class ThothAPI:
    """
    A command line interface for the Thoth python API client.
    This tool allows you to query a Thoth API for publications, works, authors
    and other endpoints.
    """

    def __init__(self):
        """
        A Thoth CLI client
        """
        self.endpoint = "https://api.thoth.pub"
        self.version = "0.8.0"

        self.thoth_email = getenv('THOTH_EMAIL')
        self.thoth_pwd = getenv('THOTH_PWD')

    def _client(self):
        """
        Returns a ThothClient object
        :return: a ThothClient
        """
        from .client import ThothClient
        return ThothClient(version=self.version, thoth_endpoint=self.endpoint)

    def _override_version(self, endpoint, version):
        """
        Allow an override of the version and endpoint on any request method
        @param endpoint: the Thoth endpoint
        @param version: the API version
        @return: None
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        self.thoth_endpoint = self.endpoint
        self.auth_endpoint = "{}/account/login".format(self.endpoint)
        self.graphql_endpoint = "{}/graphql".format(self.endpoint)
        self.client = GraphQLClient(self.graphql_endpoint)
        self.version = self.version.replace('.', '_')

    def _set_credentials(self):
        """
        Get user's Thoth credentials
        """
        print('Thoth credentials are not set.')
        print('For persistence, please set them as env variables: '
              '$THOTH_EMAIL and $THOTH_PWD')

        self.thoth_email = input('Thoth email: ')
        self.thoth_pwd = input('Thoth password: ')

    @fire.decorators.SetParseFn(_raw_parse)
    def contribution(self, contribution_id, raw=False, version=None,
                     endpoint=None, serialize=False):
        """
        Retrieves a contribution by ID from a Thoth instance
        :param str contribution_id: the contributor to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        contribution = self._client().contribution(
            contribution_id=contribution_id, raw=raw)

        if not serialize:
            print(contribution)
        else:
            print(json.dumps(contribution))

    @fire.decorators.SetParseFn(_raw_parse)
    def contributions(self, limit=100, order=None, offset=0, publishers=None,
                      contribution_type=None, raw=False, version=None,
                      endpoint=None, serialize=False):
        """
        Retrieves contributions from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str contribution_type: the contribution type (e.g. AUTHOR)
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        contribs = self._client().contributions(
            limit=limit, order=order, offset=offset, publishers=publishers,
            contribution_type=contribution_type, raw=raw)

        if not raw and not serialize:
            print(*contribs, sep='\n')
        elif serialize:
            print(json.dumps(contribs))
        else:
            print(contribs)

    @fire.decorators.SetParseFn(_raw_parse)
    def contribution_count(self, publishers=None, search=None, raw=False,
                           contribution_type=None, version=None, endpoint=None):
        """
        Retrieves a count of contributions from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str contribution_type: the work type (e.g. AUTHOR)
        :param str endpoint: a custom Thoth endpoint
        """

        self._override_version(version=version, endpoint=endpoint)

        print(self._client().contribution_count(
            publishers=publishers, search=search,
            contribution_type=contribution_type, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def contributor(self, contributor_id, raw=False, version=None,
                    endpoint=None, serialize=False):
        """
        Retrieves a contributor by ID from a Thoth instance
        :param str contributor_id: the contributor to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        contributor = self._client().contributor(contributor_id=contributor_id,
                                                 raw=raw)

        if not serialize:
            print(contributor)
        else:
            print(json.dumps(contributor))

    @fire.decorators.SetParseFn(_raw_parse)
    def contributors(self, limit=100, order=None, offset=0, search=None,
                     raw=False, version=None, endpoint=None, serialize=False):
        """
        Retrieves contributors from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        contribs = self._client().contributors(limit=limit, order=order,
                                               offset=offset,
                                               search=search,
                                               raw=raw)

        if not raw and not serialize:
            print(*contribs, sep='\n')
        elif serialize:
            print(json.dumps(contribs))
        else:
            print(contribs)

    @fire.decorators.SetParseFn(_raw_parse)
    def contributor_count(self, search=None, raw=False, version=None,
                          endpoint=None):
        """
        Retrieves a count of contributors from a Thoth instance
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """

        self._override_version(version=version, endpoint=endpoint)

        print(self._client().contributor_count(search=search, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def institution(self, institution_id, raw=False, version=None,
                    endpoint=None, serialize=False):
        """
        Retrieves an institution by ID from a Thoth instance
        :param str institution_id: the institution to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        funder = self._client().institution(institution_id=institution_id,
                                            raw=raw)

        if not serialize:
            print(funder)
        else:
            print(json.dumps(funder))

    @fire.decorators.SetParseFn(_raw_parse)
    def institutions(self, limit=100, order=None, offset=0, search=None,
                     raw=False, version=None, endpoint=None, serialize=False):
        """
        Retrieves institutions from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        funders = self._client().institutions(limit=limit, order=order,
                                              offset=offset, search=search,
                                              raw=raw)

        if not raw and not serialize:
            print(*funders, sep='\n')
        elif serialize:
            print(json.dumps(funders))
        else:
            print(funders)

    @fire.decorators.SetParseFn(_raw_parse)
    def funder_count(self, search=None, raw=False, version=None, endpoint=None):
        """
        Retrieves a count of funders from a Thoth instance
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().funder_count(search=search, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def funding(self, funding_id, raw=False, version=None, endpoint=None,
                serialize=False):
        """
        Retrieves a funding by ID from a Thoth instance
        :param str funding_id: the funding to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        funding = self._client().funding(funding_id=funding_id, raw=raw)

        if not serialize:
            print(funding)
        else:
            print(json.dumps(funding))

    @fire.decorators.SetParseFn(_raw_parse)
    def fundings(self, limit=100, order=None, offset=0, publishers=None,
                 raw=False, version=None, endpoint=None, serialize=False):
        """
        Retrieves fundings from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        fundings = self._client().fundings(limit=limit, order=order,
                                           offset=offset, publishers=publishers,
                                           raw=raw)

        if not raw and not serialize:
            print(*fundings, sep='\n')
        elif serialize:
            print(json.dumps(fundings))
        else:
            print(fundings)

    @fire.decorators.SetParseFn(_raw_parse)
    def funding_count(self, raw=False, version=None, endpoint=None):
        """
        Retrieves a count of fundings from a Thoth instance
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().funding_count(raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def imprint(self, imprint_id, raw=False, version=None, endpoint=None,
                serialize=False):
        """
        Retrieves an imprint by ID from a Thoth instance
        :param str imprint_id: the imprint to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        imprint = self._client().imprint(imprint_id=imprint_id, raw=raw)

        if not serialize:
            print(imprint)
        else:
            print(json.dumps(imprint))

    @fire.decorators.SetParseFn(_raw_parse)
    def imprints(self, limit=100, order=None, offset=0, publishers=None,
                 search=None, raw=False, version=None, endpoint=None,
                 serialize=False):
        """
        Retrieves imprints from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        imprints = self._client().imprints(limit=limit, order=order,
                                           offset=offset,
                                           publishers=publishers,
                                           search=search,
                                           raw=raw)

        if not raw and not serialize:
            print(*imprints, sep='\n')
        elif serialize:
            print(json.dumps(imprints))
        else:
            print(imprints)

    @fire.decorators.SetParseFn(_raw_parse)
    def imprint_count(self, publishers=None, search=None, raw=False,
                      version=None, endpoint=None):
        """
        Retrieves a count of imprints from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().imprint_count(publishers=publishers,
                                           search=search,
                                           raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def issue(self, issue_id, raw=False, version=None, endpoint=None,
              serialize=False):
        """
        Retrieves an issue by ID from a Thoth instance
        :param str issue_id: the issue to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        issue = self._client().issue(issue_id=issue_id, raw=raw)

        if not serialize:
            print(issue)
        else:
            print(json.dumps(issue))

    @fire.decorators.SetParseFn(_raw_parse)
    def issues(self, limit=100, order=None, offset=0, publishers=None,
               search=None, raw=False, version=None, endpoint=None,
               serialize=False):
        """
        Retrieves issues from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        issues = self._client().issues(limit=limit, order=order,
                                       offset=offset,
                                       publishers=publishers,
                                       search=search,
                                       raw=raw)

        if not raw and not serialize:
            print(*issues, sep='\n')
        elif serialize:
            print(json.dumps(issues))
        else:
            print(issues)

    @fire.decorators.SetParseFn(_raw_parse)
    def issue_count(self, raw=False, version=None, endpoint=None):
        """
        Retrieves a count of issues from a Thoth instance
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().issue_count(raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def language(self, language_id, raw=False, version=None, endpoint=None,
                 serialize=False):
        """
        Retrieves a language by ID from a Thoth instance
        :param str language_id: the language to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        lang = self._client().language(language_id=language_id, raw=raw)

        if not serialize:
            print(lang)
        else:
            print(json.dumps(lang))

    @fire.decorators.SetParseFn(_raw_parse)
    def languages(self, limit=100, order=None, offset=0, publishers=None,
                  search=None, raw=False, version=None, endpoint=None,
                  serialize=False, language_code=None, language_relation=None):
        """
        Retrieves languages from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param language_relation: select by language relation (e.g. ORIGINAL)
        :param language_code: select by language code (e.g. ADA)
        """
        self._override_version(version=version, endpoint=endpoint)

        langs = self._client().languages(limit=limit, order=order,
                                         offset=offset,
                                         publishers=publishers,
                                         search=search,
                                         language_code=language_code,
                                         language_relation=language_relation,
                                         raw=raw)

        if not raw and not serialize:
            print(*langs, sep='\n')
        elif serialize:
            print(json.dumps(langs))
        else:
            print(langs)

    @fire.decorators.SetParseFn(_raw_parse)
    def language_count(self, language_code=None, raw=False, version=None,
                       endpoint=None, language_relation=None):
        """
        Retrieves a count of languages from a Thoth instance
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param language_code: the code to retrieve (e.g. CHI)
        :param language_relation: the relation (e.g. ORIGINAL)
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().language_count(language_code=language_code,
                                            language_relation=language_relation,
                                            raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def price(self, price_id, raw=False, version=None, endpoint=None,
              serialize=False):
        """
        Retrieves a price by ID from a Thoth instance
        :param str price_id: the price to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        price = self._client().price(price_id=price_id, raw=raw)

        if not serialize:
            print(price)
        else:
            print(json.dumps(price))

    @fire.decorators.SetParseFn(_raw_parse)
    def prices(self, limit=100, order=None, offset=0, publishers=None,
               currency_code=None, raw=False, version=None, endpoint=None,
               serialize=False):
        """
        Retrieves prices from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param str currency_code: the currency code (e.g. GBP)
        """
        self._override_version(version=version, endpoint=endpoint)

        prices = self._client().prices(limit=limit, order=order,
                                       offset=offset,
                                       publishers=publishers,
                                       currency_code=currency_code,
                                       raw=raw)

        if not raw and not serialize:
            print(*prices, sep='\n')
        elif serialize:
            print(json.dumps(prices))
        else:
            print(prices)

    @fire.decorators.SetParseFn(_raw_parse)
    def price_count(self, currency_code=None, raw=False, version=None,
                    endpoint=None):
        """
        Retrieves a count of prices from a Thoth instance
        :param str currency_code: the currency to search by (e.g. GBP)
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().price_count(currency_code=currency_code, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publication(self, publication_id, raw=False,
                    version=None, endpoint=None, serialize=False):
        """
        Retrieves a publication by id from a Thoth instance
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param str publication_id: a publicationId to retrieve
        """
        self._override_version(version=version, endpoint=endpoint)

        publication = self._client().publication(publication_id=publication_id,
                                                 raw=raw)

        if not serialize:
            print(publication)
        else:
            print(json.dumps(publication))

    @fire.decorators.SetParseFn(_raw_parse)
    def publications(self, limit=100, order=None, offset=0, publishers=None,
                     search=None, publication_type=None, raw=False,
                     version=None, endpoint=None, serialize=False):
        """
        Retrieves publications from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param str publication_type: the work type (e.g. PAPERBACK)
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        pubs = self._client().publications(limit=limit, order=order,
                                           offset=offset, publishers=publishers,
                                           search=search,
                                           publication_type=publication_type,
                                           raw=raw)
        if not raw and not serialize:
            print(*pubs, sep='\n')
        elif serialize:
            print(json.dumps(pubs))
        else:
            print(pubs)

    @fire.decorators.SetParseFn(_raw_parse)
    def publication_count(self, publishers=None, search=None, raw=False,
                          publication_type=None, version=None, endpoint=None):
        """
        Retrieves a count of publications from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str publication_type: the work type (e.g. MONOGRAPH)
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().publication_count(
            publishers=publishers, search=search,
            publication_type=publication_type, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publisher(self, publisher_id, raw=False, version=None, endpoint=None,
                  serialize=False):
        """
        Retrieves a publisher by ID from a Thoth instance
        :param str publisher_id: the publisher to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        publisher = self._client().publisher(publisher_id=publisher_id, raw=raw)

        if not serialize:
            print(publisher)
        else:
            print(json.dumps(publisher))

    @fire.decorators.SetParseFn(_raw_parse)
    def publishers(self, limit=100, order=None, offset=0, publishers=None,
                   search=None, raw=False, version=None, endpoint=None,
                   serialize=False):
        """
        Retrieves publishers from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        found_publishers = self._client().publishers(limit=limit, order=order,
                                                     offset=offset,
                                                     publishers=publishers,
                                                     search=search,
                                                     raw=raw)

        if not raw and not serialize:
            print(*found_publishers, sep='\n')
        elif serialize:
            print(json.dumps(found_publishers))
        else:
            print(found_publishers)

    @fire.decorators.SetParseFn(_raw_parse)
    def publisher_count(self, publishers=None, search=None, raw=False,
                        version=None, endpoint=None):
        """
        Retrieves a count of publishers from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().publisher_count(publishers=publishers,
                                             search=search,
                                             raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def series(self, series_id, raw=False, version=None, endpoint=None,
               serialize=False):
        """
        Retrieves a series by ID from a Thoth instance
        :param str series_id: the series to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        series = self._client().series(series_id=series_id, raw=raw)

        if not serialize:
            print(series)
        else:
            print(json.dumps(series))

    @fire.decorators.SetParseFn(_raw_parse)
    def serieses(self, limit=100, order=None, offset=0, publishers=None,
                 search=None, series_type=None, raw=False, version=None,
                 endpoint=None, serialize=False):
        """
        Retrieves serieses from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param series_type: the type of serieses to return (e.g. BOOK_SERIES)
        """
        self._override_version(version=version, endpoint=endpoint)

        serieses = self._client().serieses(limit=limit, order=order,
                                           offset=offset,
                                           publishers=publishers,
                                           search=search,
                                           series_type=series_type,
                                           raw=raw)

        if not raw and not serialize:
            print(*serieses, sep='\n')
        elif serialize:
            print(json.dumps(serieses))
        else:
            print(serieses)

    @fire.decorators.SetParseFn(_raw_parse)
    def series_count(self, publishers=None, search=None, raw=False,
                     series_type=None, version=None, endpoint=None):
        """
        Retrieves a count of serieses from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str series_type: the work type (e.g. BOOK_SERIES)
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().series_count(publishers=publishers, search=search,
                                          series_type=series_type, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def subject(self, subject_id, raw=False, version=None, endpoint=None,
                serialize=False):
        """
        Retrieves a subject by ID from a Thoth instance
        :param str subject_id: the subject to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        subj = self._client().subject(subject_id=subject_id, raw=raw)

        if not serialize:
            print(subj)
        else:
            print(json.dumps(subj))

    @fire.decorators.SetParseFn(_raw_parse)
    def subjects(self, limit=100, order=None, offset=0, publishers=None,
                 search=None, raw=False, version=None, endpoint=None,
                 serialize=False, subject_type=None):
        """
        Retrieves subjects from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param subject_type: select by subject code (e.g. BIC)
        """
        self._override_version(version=version, endpoint=endpoint)

        subj = self._client().subjects(limit=limit, order=order,
                                       offset=offset,
                                       publishers=publishers,
                                       search=search,
                                       subject_type=subject_type,
                                       raw=raw)

        if not raw and not serialize:
            print(*subj, sep='\n')
        elif serialize:
            print(json.dumps(subj))
        else:
            print(subj)

    @fire.decorators.SetParseFn(_raw_parse)
    def subject_count(self, subject_type=None, raw=False, version=None,
                      endpoint=None, search=None):
        """
        Retrieves a count of subjects from a Thoth instance
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param str subject_type: the type to retrieve (e.g. BIC)
        :param str search: a search
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().subject_count(subject_type=subject_type,
                                           search=search, raw=raw))

    def supported_versions(self):
        """
        Retrieves a list of supported Thoth versions
        @return: a list of supported Thoth versions
        """
        return self._client().supported_versions()

    @fire.decorators.SetParseFn(_raw_parse)
    def work(self, doi=None, work_id=None, raw=False, version=None,
             endpoint=None, serialize=False, cover_ascii=False):
        """
        Retrieves a work by DOI or ID from a Thoth instance
        :param str doi: the doi to fetch
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param str work_id: a workId to retrieve
        :param bool cover_ascii: whether to render an ASCII art cover
        """
        self._override_version(version=version, endpoint=endpoint)

        if not doi and not work_id:
            print("You must specify either workId or doi.")
            return
        elif doi:
            work = self._client().work_by_doi(doi=doi, raw=raw)
        else:
            work = self._client().work_by_id(work_id=work_id, raw=raw)

        if not serialize:
            print(work)
        else:
            print(json.dumps(work))

        if cover_ascii:
            # just for lolz
            import ascii_magic
            output = ascii_magic.from_url(work.coverUrl, columns=85)
            ascii_magic.to_terminal(output)

    @fire.decorators.SetParseFn(_raw_parse)
    def works(self, limit=100, order=None, offset=0, publishers=None,
              search=None, work_type=None, work_status=None, raw=False,
              version=None, endpoint=None, serialize=False):
        """
        Retrieves works from a Thoth instance
        :param int limit: the maximum number of results to return
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param str work_type: the work type (e.g. MONOGRAPH)
        :param str work_status: the work status (e.g. ACTIVE)
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        self._override_version(version=version, endpoint=endpoint)

        works = self._client().works(limit=limit, order=order, offset=offset,
                                     publishers=publishers,
                                     search=search,
                                     work_type=work_type,
                                     work_status=work_status,
                                     raw=raw)

        if not raw and not serialize:
            print(*works, sep='\n')
        elif serialize:
            print(json.dumps(works))
        elif raw:
            print(works)

    @fire.decorators.SetParseFn(_raw_parse)
    def work_count(self, publishers=None, search=None, raw=False,
                   work_type=None, work_status=None, version=None,
                   endpoint=None):
        """
        Retrieves a count of works from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str search: a search string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str work_type: the work type (e.g. MONOGRAPH)
        :param str work_status: the work status (e.g. ACTIVE)
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        print(self._client().work_count(publishers=publishers,
                                        search=search,
                                        work_type=work_type,
                                        work_status=work_status,
                                        raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def update_cover(self, doi=None, work_id=None, url=None, version=None,
                     endpoint=None):
        """
        Update the work cover by DOI or ID
        :param str doi: the doi of the work
        :param str work_id: the workId of the work
        :param str url: the cover URL of the work
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        self._override_version(version=version, endpoint=endpoint)

        client = self._client()

        if not url:
            print("You must specify a cover URL.")
            return

        if not doi and not work_id:
            print("You must specify either workId or doi.")
            return
        elif doi:
            work = client.work_by_doi(doi=doi, raw=True)
            work_obj = json.loads(work)
            data = work_obj['data']['workByDoi']
        else:
            work = client.work_by_id(work_id=work_id, raw=True)
            work_obj = json.loads(work)
            data = work_obj['data']['work']

        # Update cover URL
        data['coverUrl'] = url

        if not self.thoth_email or not self.thoth_pwd:
            self._set_credentials()

        client.login(self.thoth_email, self.thoth_pwd)

        mutation = client.mutation('updateWork', data)


if __name__ == '__main__':
    fire.Fire(ThothAPI)

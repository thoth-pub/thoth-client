"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""

import fire


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
        self.version = "0.4.2"

    def _client(self):
        """
        Returns a ThothClient object
        :return: a ThothClient
        """
        from .client import ThothClient
        return ThothClient(version=self.version, thoth_endpoint=self.endpoint)

    @fire.decorators.SetParseFn(_raw_parse)
    def contributions(self, limit=100, order=None, offset=0, publishers=None,
                      filter_str=None, contribution_type=None, raw=False,
                      version=None, endpoint=None):
        """
        Retrieves works from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param str contribution_type: the contribution type (e.g. AUTHOR)
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        contribs = self._client().contributions(limit=limit, order=order,
                                                offset=offset,
                                                publishers=publishers,
                                                filter_str=filter_str,
                                                contribution_type=
                                                contribution_type,
                                                raw=raw)

        if not raw:
            print(*contribs, sep='\n')
        else:
            print(contribs)

    @fire.decorators.SetParseFn(_raw_parse)
    def works(self, limit=100, order=None, offset=0, publishers=None,
              filter_str=None, work_type=None, work_status=None, raw=False,
              version=None, endpoint=None):
        """
        Retrieves works from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param str work_type: the work type (e.g. MONOGRAPH)
        :param str work_status: the work status (e.g. ACTIVE)
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        works = self._client().works(limit=limit, order=order, offset=offset,
                                     publishers=publishers,
                                     filter_str=filter_str,
                                     work_type=work_type,
                                     work_status=work_status,
                                     raw=raw)
        if not raw:
            print(*works, sep='\n')
        else:
            print(works)

    @fire.decorators.SetParseFn(_raw_parse)
    def work(self, doi, raw=False, version=None, endpoint=None):
        """
        Retrieves a work by DOI from a Thoth instance
        :param str doi: the doi to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().work_by_doi(doi=doi, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publisher(self, publisher_id, raw=False, version=None, endpoint=None):
        """
        Retrieves a work by DOI from a Thoth instance
        :param str publisher_id: the publisher to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().publisher(publisher_id=publisher_id, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publishers(self, limit=100, order=None, offset=0, publishers=None,
                   filter_str=None, raw=False, version=None, endpoint=None):
        """
        Retrieves publishers from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        publishers = self._client().publishers(limit=limit, order=order,
                                               offset=offset,
                                               publishers=publishers,
                                               filter_str=filter_str,
                                               raw=raw)

        if not raw:
            print(*publishers, sep='\n')
        else:
            print(publishers)

    @fire.decorators.SetParseFn(_raw_parse)
    def publisher_count(self, publishers=None, filter_str=None, raw=False,
                        version=None, endpoint=None):
        """
        Retrieves a count of publishers from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().publisher_count(publishers=publishers,
                                             filter_str=filter_str,
                                             raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def work_count(self, publishers=None, filter_str=None, raw=False,
                   work_type=None, work_status=None, version=None,
                   endpoint=None):
        """
        Retrieves a count of works from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str work_type: the work type (e.g. MONOGRAPH)
        :param str work_status: the work status (e.g. ACTIVE)
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().work_count(publishers=publishers,
                                        filter_str=filter_str,
                                        work_type=work_type,
                                        work_status=work_status,
                                        raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publication_count(self, publishers=None, filter_str=None, raw=False,
                          publication_type=None, version=None, endpoint=None):
        """
        Retrieves a count of publications from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str publication_type: the work type (e.g. MONOGRAPH)
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().publication_count(publishers=publishers,
                                               filter_str=filter_str,
                                               publication_type=publication_type,
                                               raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def contribution_count(self, publishers=None, filter_str=None, raw=False,
                           contribution_type=None, version=None, endpoint=None):
        """
        Retrieves a count of publications from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str contribution_type: the work type (e.g. AUTHOR)
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().contribution_count(publishers=publishers,
                                                filter_str=filter_str,
                                                contribution_type=contribution_type,
                                                raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publications(self, limit=100, order=None, offset=0, publishers=None,
                     filter_str=None, publication_type=None, raw=False,
                     version=None, endpoint=None):
        """
        Retrieves publications from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter_str: a filter string to search
        :param str publication_type: the work type (e.g. PAPERBACK)
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        pubs = self._client().publications(limit=limit, order=order,
                                           offset=offset, publishers=publishers,
                                           filter_str=filter_str,
                                           publication_type=publication_type,
                                           raw=raw)
        if not raw:
            print(*pubs, sep='\n')
        else:
            print(pubs)


if __name__ == '__main__':
    fire.Fire(ThothAPI)

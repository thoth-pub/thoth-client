"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json

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
                      contribution_type=None, raw=False, version=None,
                      endpoint=None, serialize=False):
        """
        Retrieves works from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str contribution_type: the contribution type (e.g. AUTHOR)
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        contribs = self._client().contributions(limit=limit, order=order,
                                                offset=offset,
                                                publishers=publishers,
                                                contribution_type=
                                                contribution_type,
                                                raw=raw)

        if not raw and not serialize:
            print(*contribs, sep='\n')
        elif serialize:
            print(json.dumps(contribs))
        else:
            print(contribs)

    @fire.decorators.SetParseFn(_raw_parse)
    def contributors(self, limit=100, order=None, offset=0, filter=None,
                     raw=False, version=None, endpoint=None, serialize=False):
        """
        Retrieves contributors from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        contribs = self._client().contributors(limit=limit, order=order,
                                               offset=offset,
                                               filter=filter,
                                               raw=raw)

        if not raw and not serialize:
            print(*contribs, sep='\n')
        elif serialize:
            print(json.dumps(contribs))
        else:
            print(contribs)

    @fire.decorators.SetParseFn(_raw_parse)
    def works(self, limit=100, order=None, offset=0, publishers=None,
              filter=None, work_type=None, work_status=None, raw=False,
              version=None, endpoint=None, serialize=False):
        """
        Retrieves works from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param str work_type: the work type (e.g. MONOGRAPH)
        :param str work_status: the work status (e.g. ACTIVE)
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        works = self._client().works(limit=limit, order=order, offset=offset,
                                     publishers=publishers,
                                     filter=filter,
                                     work_type=work_type,
                                     work_status=work_status,
                                     raw=raw)

        if not raw and not serialize:
            print(*works, sep='\n')
        elif serialize:
            print(json.dumps(works))
        elif raw:
            print(works)

    def supported_versions(self):
        """
        Retrieves a list of supported Thoth versions
        @return: a list of supported Thoth versions
        """
        return self._client().supported_versions()

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
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        publication = self._client().publication(publication_id=publication_id,
                                                 raw=raw)

        if not serialize:
            print(publication)
        else:
            print(json.dumps(publication))

    @fire.decorators.SetParseFn(_raw_parse)
    def work(self, doi=None, work_id=None, raw=False, version=None,
             endpoint=None, serialize=False, cover_ascii=False):
        """
        Retrieves a work by DOI from a Thoth instance
        :param str doi: the doi to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param str work_id: a workId to retrieve
        :param bool cover_ascii: whether to render an ASCII art cover
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

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
    def publisher(self, publisher_id, raw=False, version=None, endpoint=None,
                  serialize=False):
        """
        Retrieves a publisher by ID from a Thoth instance
        :param str publisher_id: the publisher to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        publisher = self._client().publisher(publisher_id=publisher_id, raw=raw)

        if not serialize:
            print(publisher)
        else:
            print(json.dumps(publisher))

    @fire.decorators.SetParseFn(_raw_parse)
    def contributor(self, contributor_id, raw=False, version=None,
                    endpoint=None, serialize=False):
        """
        Retrieves a contriibutor by ID from a Thoth instance
        :param str contributor_id: the contributor to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        contributor = self._client().contributor(contributor_id=contributor_id,
                                                 raw=raw)

        if not serialize:
            print(contributor)
        else:
            print(json.dumps(contributor))

    @fire.decorators.SetParseFn(_raw_parse)
    def contribution(self, contribution_id, raw=False, version=None,
                     endpoint=None, serialize=False):
        """
        Retrieves a contribution by ID from a Thoth instance
        :param str contribution_id: the contributor to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        contribution = self._client().contribution(contribution_id=
                                                   contribution_id,
                                                   raw=raw)

        if not serialize:
            print(contribution)
        else:
            print(json.dumps(contribution))

    @fire.decorators.SetParseFn(_raw_parse)
    def imprint(self, imprint_id, raw=False, version=None, endpoint=None,
                serialize=False):
        """
        Retrieves a publisher by ID from a Thoth instance
        :param str imprint_id: the imprint to fetch
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        imprint = self._client().imprint(imprint_id=imprint_id, raw=raw)

        if not serialize:
            print(imprint)
        else:
            print(json.dumps(imprint))

    @fire.decorators.SetParseFn(_raw_parse)
    def publishers(self, limit=100, order=None, offset=0, publishers=None,
                   filter=None, raw=False, version=None, endpoint=None,
                   serialize=False):
        """
        Retrieves publishers from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        found_publishers = self._client().publishers(limit=limit, order=order,
                                                     offset=offset,
                                                     publishers=publishers,
                                                     filter=filter,
                                                     raw=raw)

        if not raw and not serialize:
            print(*found_publishers, sep='\n')
        elif serialize:
            print(json.dumps(found_publishers))
        else:
            print(found_publishers)

    @fire.decorators.SetParseFn(_raw_parse)
    def imprints(self, limit=100, order=None, offset=0, publishers=None,
                 filter=None, raw=False, version=None, endpoint=None,
                 serialize=False):
        """
        Retrieves imprints from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        imprints = self._client().imprints(limit=limit, order=order,
                                           offset=offset,
                                           publishers=publishers,
                                           filter=filter,
                                           raw=raw)

        if not raw and not serialize:
            print(*imprints, sep='\n')
        elif serialize:
            print(json.dumps(imprints))
        else:
            print(imprints)

    @fire.decorators.SetParseFn(_raw_parse)
    def serieses(self, limit=100, order=None, offset=0, publishers=None,
                 filter=None, series_type=None, raw=False, version=None,
                 endpoint=None, serialize=False):
        """
        Retrieves serieses from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        :param series_type: the type of serieses to return (e.g. BOOK_SERIES)
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        serieses = self._client().serieses(limit=limit, order=order,
                                           offset=offset,
                                           publishers=publishers,
                                           filter=filter,
                                           series_type=series_type,
                                           raw=raw)

        if not raw and not serialize:
            print(*serieses, sep='\n')
        elif serialize:
            print(json.dumps(serieses))
        else:
            print(serieses)

    @fire.decorators.SetParseFn(_raw_parse)
    def contributor_count(self, filter=None, raw=False, version=None,
                          endpoint=None):
        """
        Retrieves a count of contributors from a Thoth instance
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().contributor_count(filter=filter, raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publisher_count(self, publishers=None, filter=None, raw=False,
                        version=None, endpoint=None):
        """
        Retrieves a count of publishers from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().publisher_count(publishers=publishers,
                                             filter=filter,
                                             raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def imprint_count(self, publishers=None, filter=None, raw=False,
                      version=None, endpoint=None):
        """
        Retrieves a count of imprints from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        """

        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        print(self._client().imprint_count(publishers=publishers,
                                           filter=filter,
                                           raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def work_count(self, publishers=None, filter=None, raw=False,
                   work_type=None, work_status=None, version=None,
                   endpoint=None):
        """
        Retrieves a count of works from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
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
                                        filter=filter,
                                        work_type=work_type,
                                        work_status=work_status,
                                        raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publication_count(self, publishers=None, filter=None, raw=False,
                          publication_type=None, version=None, endpoint=None):
        """
        Retrieves a count of publications from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
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
                                               filter=filter,
                                               publication_type=publication_type,
                                               raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def contribution_count(self, publishers=None, filter=None, raw=False,
                           contribution_type=None, version=None, endpoint=None):
        """
        Retrieves a count of publications from a Thoth instance
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
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
                                                filter=filter,
                                                contribution_type=contribution_type,
                                                raw=raw))

    @fire.decorators.SetParseFn(_raw_parse)
    def publications(self, limit=100, order=None, offset=0, publishers=None,
                     filter=None, publication_type=None, raw=False,
                     version=None, endpoint=None, serialize=False):
        """
        Retrieves publications from a Thoth instance
        :param int limit: the maximum number of results to return (default: 100)
        :param int order: a GraphQL order query statement
        :param int offset: the offset from which to retrieve results (default: 0)
        :param str publishers: a list of publishers to limit by
        :param str filter: a filter string to search
        :param str publication_type: the work type (e.g. PAPERBACK)
        :param bool raw: whether to return a python object or the raw server result
        :param str version: a custom Thoth version
        :param str endpoint: a custom Thoth endpoint
        :param bool serialize: return a pickled python object
        """
        if endpoint:
            self.endpoint = endpoint

        if version:
            self.version = version

        pubs = self._client().publications(limit=limit, order=order,
                                           offset=offset, publishers=publishers,
                                           filter=filter,
                                           publication_type=publication_type,
                                           raw=raw)
        if not raw and not serialize:
            print(*pubs, sep='\n')
        elif serialize:
            print(json.dumps(pubs))
        else:
            print(pubs)


if __name__ == '__main__':
    fire.Fire(ThothAPI)

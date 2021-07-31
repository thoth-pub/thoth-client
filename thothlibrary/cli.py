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
    @param value: the input value
    @return: the parsed value
    """
    return value


class ThothAPI:
    def _client(self):
        """
        Returns a ThothClient object
        @return: a ThothClient
        """
        from client import ThothClient
        return ThothClient(version="0.4.2")

    @fire.decorators.SetParseFn(_raw_parse)
    def works(self, limit=100, order=None, offset=0, publishers=None,
              filter_str=None, work_type=None, work_status=None, raw=False):
        """
        A list of works
        @param limit: the maximum number of results to return
        @param order: a GraphQL order query statement
        @param offset: the offset from which to retrieve results
        @param publishers: a list of publishers to limit by
        @param filter_str: a filter string to search
        @param work_type: the work type (e.g. MONOGR++APH)
        @param work_status: the work status (e.g. ACTIVE)
        @param raw: whether to return a python object or the raw server result
        """
        print(*self._client().works(limit=limit, order=order, offset=offset,
                                    publishers=publishers,
                                    filter_str=filter_str,
                                    work_type=work_type,
                                    work_status=work_status,
                                    raw=raw), sep='\n')


    def publishers(self, json=False):
        """
        Full list of metadata formats that can be output by Thoth
        @param json: whether to return JSON or an object (default)
        """
        print(_client().publishers())


if __name__ == '__main__':
    fire.Fire(ThothAPI)

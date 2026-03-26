"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import importlib
import json
from os import getenv

import fire

import thothlibrary

_V1_ENDPOINTS = importlib.import_module("thothlibrary.thoth-1_0_0.endpoints")
COUNT_QUERIES = _V1_ENDPOINTS.COUNT_QUERIES
LIST_QUERIES = _V1_ENDPOINTS.LIST_QUERIES
SINGLE_DOI_QUERIES = _V1_ENDPOINTS.SINGLE_DOI_QUERIES
SINGLE_ID_QUERIES = _V1_ENDPOINTS.SINGLE_ID_QUERIES


def _raw_parse(value):
    return value


def _serialise(value):
    return json.dumps(value)


class ThothAPI:
    """A command line interface for the Thoth python API client."""

    def __init__(self):
        self.endpoint = "https://api.thoth.pub"
        self.thoth_pat = getenv("THOTH_PAT")

    def _client(self):
        from .client import ThothClient
        return ThothClient(thoth_endpoint=self.endpoint)

    def _override_endpoint(self, endpoint):
        if endpoint:
            self.endpoint = endpoint

    def _set_token(self):
        print("A Thoth PAT is required for this command.")
        print("For persistence, please set it as the env variable: $THOTH_PAT")

        self.thoth_pat = input("Thoth PAT: ")

    @staticmethod
    def _emit(result, raw=False, serialize=False):
        if serialize:
            print(_serialise(result))
            return
        if raw:
            print(result)
            return
        if isinstance(result, list):
            print(*result, sep="\n")
            return
        print(result)

    def supported_versions(self):
        print(*thothlibrary.ThothClient.supported_versions(), sep="\n")

    @fire.decorators.SetParseFn(_raw_parse)
    def work(self, doi=None, work_id=None, raw=False,
             endpoint=None, serialize=False):
        self._override_endpoint(endpoint=endpoint)
        client = self._client()

        if doi:
            result = client.work_by_doi(doi=doi, raw=raw)
        elif work_id:
            result = client.work_by_id(work_id=work_id, raw=raw)
        else:
            print("You must specify either --doi or --work_id.")
            return

        self._emit(result, raw=raw, serialize=serialize)

    @fire.decorators.SetParseFn(_raw_parse)
    def update_cover(self, doi=None, work_id=None, url=None, endpoint=None):
        self._override_endpoint(endpoint=endpoint)

        client = self._client()

        if not url:
            print("You must specify a cover URL.")
            return

        if not doi and not work_id:
            print("You must specify either workId or doi.")
            return
        if doi:
            work = client.work_by_doi(doi=doi, raw=True)
            data = json.loads(work)["data"]["workByDoi"]
        else:
            work = client.work_by_id(work_id=work_id, raw=True)
            data = json.loads(work)["data"]["work"]

        data["coverUrl"] = url

        if not self.thoth_pat:
            self._set_token()

        client.set_token(self.thoth_pat)
        print(client.mutation("updateWork", data))


def _query_cli_method(client_method):
    @fire.decorators.SetParseFn(_raw_parse)
    def _method(self, raw=False, endpoint=None, serialize=False, **kwargs):
        self._override_endpoint(endpoint=endpoint)
        result = getattr(self._client(), client_method)(raw=raw, **kwargs)
        self._emit(result, raw=raw, serialize=serialize)

    return _method


for method_name in sorted(
    set(SINGLE_ID_QUERIES) |
    set(SINGLE_DOI_QUERIES) |
    set(LIST_QUERIES) |
    set(COUNT_QUERIES) |
    {"bookIds"}
):
    setattr(ThothAPI, method_name, _query_cli_method(method_name))


if __name__ == "__main__":
    fire.Fire(ThothAPI)

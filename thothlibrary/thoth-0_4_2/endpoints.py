"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from client import ThothClient


class ThothClient0_4_2(ThothClient):

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
                "coverUrl",
                "coverCaption",
                "publications { isbn publicationType }",
                "contributions { fullName contributionType mainContribution contributionOrdinal }",
                "imprint { publisher { publisherName publisherId } }",
                "__typename"
            ]
        },

        "publishers": {
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
                "imprints { imprintUrl imprintId imprintName}"
                "updatedAt",
                "createdAt",
                "publisherId",
                "publisherName",
                "publisherShortname",
                "publisherUrl",
            ]
        }
    }

    def __init__(self, input_class):
        super().__init__()

        # this is the magic dynamic generation part that wires up the methods
        input_class.works = getattr(self, 'works')
        input_class.QUERIES = getattr(self, 'QUERIES')

    def works(self, limit: int = 100, offset: int = 0, filter_str: str = "",
              order: str = None, publishers: str = None, work_type: str = None,
              work_status: str = None, raw: bool = False):
        """Construct and trigger a query to obtain all works"""
        if order is None:
            order = {}
        parameters = {
            "offset": offset,
            "limit": limit,
        }

        if filter_str:
            parameters["filter"] = filter_str

        if order:
            parameters["order"] = order

        if publishers:
            parameters["publishers"] = publishers

        if work_type:
            parameters["workType"] = work_type

        if work_status:
            parameters["workStatus"] = work_status

        return self._api_request("works", parameters, return_raw=raw)

    def publishers(self, limit: int = 100, offset: int = 0,
                   filter_str: str = ""):
        """Construct and trigger a query to obtain all publishers"""
        parameters = {
            "limit": limit,
            "offset": offset,
            "filter": filter_str,
        }
        return self.query("publishers", parameters)

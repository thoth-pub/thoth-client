"""
Copyright (c) 2026 Thoth Open Metadata
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""

from .queries import QUERIES


SINGLE_ID_QUERIES = {
    "contribution": ("contribution", "contribution_id", "contributionId"),
    "contributor": ("contributor", "contributor_id", "contributorId"),
    "institution": ("institution", "institution_id", "institutionId"),
    "funding": ("funding", "funding_id", "fundingId"),
    "imprint": ("imprint", "imprint_id", "imprintId"),
    "issue": ("issue", "issue_id", "issueId"),
    "language": ("language", "language_id", "languageId"),
    "location": ("location", "location_id", "locationId"),
    "price": ("price", "price_id", "priceId"),
    "publication": ("publication", "publication_id", "publicationId"),
    "publisher": ("publisher", "publisher_id", "publisherId"),
    "series": ("series", "series_id", "seriesId"),
    "subject": ("subject", "subject_id", "subjectId"),
    "file": ("file", "file_id", "fileId"),
    "affiliation": ("affiliation", "affiliation_id", "affiliationId"),
    "reference": ("reference", "reference_id", "referenceId"),
    "additional_resource": (
        "additionalResource", "additional_resource_id", "additionalResourceId"
    ),
    "award": ("award", "award_id", "awardId"),
    "endorsement": ("endorsement", "endorsement_id", "endorsementId"),
    "book_review": ("bookReview", "book_review_id", "bookReviewId"),
    "work_featured_video": (
        "workFeaturedVideo", "work_featured_video_id", "workFeaturedVideoId"
    ),
    "contact": ("contact", "contact_id", "contactId"),
    "work_by_id": ("work", "work_id", "workId"),
    "title": ("title", "title_id", "titleId"),
    "abstract": ("abstract", "abstract_id", "abstractId"),
    "biography": ("biography", "biography_id", "biographyId"),
}

SINGLE_DOI_QUERIES = {
    "work_by_doi": ("workByDoi", "doi"),
    "book_by_doi": ("bookByDoi", "doi"),
    "chapter_by_doi": ("chapterByDoi", "doi"),
}

LIST_QUERIES = {
    "contributions": (
        "contributions",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers", "contribution_types": "contributionTypes"}
    ),
    "contributors": (
        "contributors",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order"}
    ),
    "institutions": (
        "institutions",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order"}
    ),
    "fundings": (
        "fundings",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "imprints": (
        "imprints",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers"}
    ),
    "issues": (
        "issues",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "languages": (
        "languages",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers", "language_codes": "languageCodes",
         "language_relation": "languageRelation",
         "language_relations": "languageRelations"}
    ),
    "locations": (
        "locations",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers",
         "location_platforms": "locationPlatforms"}
    ),
    "prices": (
        "prices",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers", "currency_codes": "currencyCodes"}
    ),
    "publications": (
        "publications",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers",
         "publication_types": "publicationTypes"}
    ),
    "publishers": (
        "publishers",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers"}
    ),
    "references": (
        "references",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "serieses": (
        "serieses",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers",
         "series_types": "seriesTypes"}
    ),
    "subjects": (
        "subjects",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers",
         "subject_types": "subjectTypes"}
    ),
    "works": (
        "works",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers",
         "work_types": "workTypes", "work_status": "workStatus",
         "work_statuses": "workStatuses",
         "publication_date": "publicationDate",
         "updated_at_with_relations": "updatedAtWithRelations"}
    ),
    "books": (
        "books",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers",
         "work_status": "workStatus", "work_statuses": "workStatuses",
         "publication_date": "publicationDate",
         "updated_at_with_relations": "updatedAtWithRelations"}
    ),
    "chapters": (
        "chapters",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "publishers": "publishers",
         "work_status": "workStatus", "work_statuses": "workStatuses",
         "publication_date": "publicationDate",
         "updated_at_with_relations": "updatedAtWithRelations"}
    ),
    "affiliations": (
        "affiliations",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "additional_resources": (
        "additionalResources",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "awards": (
        "awards",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "endorsements": (
        "endorsements",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "book_reviews": (
        "bookReviews",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "work_featured_videos": (
        "workFeaturedVideos",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers"}
    ),
    "titles": (
        "titles",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "locale_codes": "localeCodes",
         "markup_format": "markupFormat"}
    ),
    "abstracts": (
        "abstracts",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "locale_codes": "localeCodes",
         "markup_format": "markupFormat"}
    ),
    "biographies": (
        "biographies",
        {"limit": "limit", "offset": "offset", "search": "filter",
         "order": "order", "locale_codes": "localeCodes",
         "markup_format": "markupFormat"}
    ),
    "contacts": (
        "contacts",
        {"limit": "limit", "offset": "offset", "order": "order",
         "publishers": "publishers", "contact_types": "contactTypes"}
    ),
}

COUNT_QUERIES = {
    "contribution_count": (
        "contributionCount", {"contribution_types": "contributionTypes"}
    ),
    "contributor_count": ("contributorCount", {"search": "filter"}),
    "institution_count": ("institutionCount", {"search": "filter"}),
    "funding_count": ("fundingCount", {}),
    "imprint_count": (
        "imprintCount", {"search": "filter", "publishers": "publishers"}
    ),
    "issue_count": ("issueCount", {}),
    "language_count": (
        "languageCount",
        {"language_codes": "languageCodes",
         "language_relation": "languageRelation",
         "language_relations": "languageRelations"}
    ),
    "location_count": ("locationCount",
                        {"location_platforms": "locationPlatforms"}),
    "price_count": ("priceCount", {"currency_codes": "currencyCodes"}),
    "publication_count": (
        "publicationCount",
        {"search": "filter", "publishers": "publishers",
         "publication_types": "publicationTypes"}
    ),
    "publisher_count": (
        "publisherCount", {"search": "filter", "publishers": "publishers"}
    ),
    "series_count": (
        "seriesCount",
        {"search": "filter", "publishers": "publishers",
         "series_types": "seriesTypes"}
    ),
    "subject_count": (
        "subjectCount", {"search": "filter", "subject_types": "subjectTypes"}
    ),
    "work_count": (
        "workCount",
        {"search": "filter", "publishers": "publishers",
         "work_types": "workTypes", "work_status": "workStatus",
         "work_statuses": "workStatuses",
         "publication_date": "publicationDate",
         "updated_at_with_relations": "updatedAtWithRelations"}
    ),
    "book_count": (
        "bookCount",
        {"search": "filter", "publishers": "publishers",
         "work_status": "workStatus", "work_statuses": "workStatuses",
         "publication_date": "publicationDate",
         "updated_at_with_relations": "updatedAtWithRelations"}
    ),
    "chapter_count": (
        "chapterCount",
        {"search": "filter", "publishers": "publishers",
         "work_status": "workStatus", "work_statuses": "workStatuses",
         "publication_date": "publicationDate",
         "updated_at_with_relations": "updatedAtWithRelations"}
    ),
    "affiliation_count": ("affiliationCount", {}),
    "reference_count": ("referenceCount", {}),
    "additional_resource_count": ("additionalResourceCount", {}),
    "award_count": ("awardCount", {}),
    "endorsement_count": ("endorsementCount", {}),
    "book_review_count": ("bookReviewCount", {}),
    "work_featured_video_count": ("workFeaturedVideoCount", {}),
    "contact_count": ("contactCount", {"contact_types": "contactTypes"}),
}


class ThothClient1_0_0:
    """v1 query helpers attached onto the main client."""

    @staticmethod
    def _quote(value):
        if value is None:
            return None
        value = str(value)
        if value.startswith('"') and value.endswith('"'):
            return value
        return '"{0}"'.format(value)

    def _query_parameters(self, kwargs, mapping):
        parameters = {}
        if "limit" in mapping:
            parameters["limit"] = kwargs.get("limit", 100)
        if "offset" in mapping:
            parameters["offset"] = kwargs.get("offset", 0)

        for py_name, gql_name in mapping.items():
            if py_name in {"limit", "offset"}:
                continue
            value = kwargs.get(py_name)
            if py_name == "search" and value and not str(value).startswith('"'):
                value = self._quote(value)
            self._dictionary_append(parameters, gql_name, value)

        return parameters

    def _single_id_request(self, query_name, gql_name, value, raw=False,
                           **extra_parameters):
        parameters = {gql_name: self._quote(value)}
        for key, extra_value in extra_parameters.items():
            self._dictionary_append(parameters, key, extra_value)
        return self._api_request(query_name, parameters, return_raw=raw)

    def _single_doi_request(self, query_name, doi, raw=False):
        return self._api_request(query_name, {"doi": self._quote(doi)},
                                 return_raw=raw)

    def bookIds(self, limit=100, offset=0, search="", order=None,
                publishers=None, work_status=None, work_statuses=None,
                publication_date=None, updated_at_with_relations=None,
                raw=False):
        parameters = self._query_parameters(
            {
                "limit": limit,
                "offset": offset,
                "search": search,
                "order": order,
                "publishers": publishers,
                "work_status": work_status,
                "work_statuses": work_statuses,
                "publication_date": publication_date,
                "updated_at_with_relations": updated_at_with_relations,
            },
            LIST_QUERIES["books"][1],
        )

        response = self.query("books", parameters, raw=raw)
        if raw:
            return response

        ids = [
            {"workId": item["workId"], "__typename": item.get("__typename",
             "Work")}
            for item in response
        ]
        return self._build_structure("bookIds", ids)


def _single_id_method(query_name, arg_name, gql_arg_name, markup=False):
    def _method(self, raw=False, **kwargs):
        extra_parameters = {}
        if markup and kwargs.get("markup_format"):
            extra_parameters["markupFormat"] = kwargs["markup_format"]
        return self._single_id_request(query_name, gql_arg_name,
                                       kwargs[arg_name], raw=raw,
                                       **extra_parameters)

    return _method


def _single_doi_method(query_name, arg_name):
    def _method(self, raw=False, **kwargs):
        return self._single_doi_request(query_name, kwargs[arg_name], raw=raw)

    return _method


def _list_method(query_name, mapping):
    def _method(self, raw=False, **kwargs):
        return self._api_request(
            query_name,
            self._query_parameters(kwargs, mapping),
            return_raw=raw,
        )

    return _method


def _count_method(query_name, mapping):
    def _method(self, raw=False, **kwargs):
        return self._api_request(
            query_name,
            self._query_parameters(kwargs, mapping),
            return_raw=raw,
        )

    return _method


for method_name, (query_name, arg_name, gql_arg_name) in SINGLE_ID_QUERIES.items():
    setattr(
        ThothClient1_0_0,
        method_name,
        _single_id_method(
            query_name,
            arg_name,
            gql_arg_name,
            markup=method_name in {"title", "abstract", "biography"},
        ),
    )

for method_name, (query_name, arg_name) in SINGLE_DOI_QUERIES.items():
    setattr(ThothClient1_0_0, method_name,
            _single_doi_method(query_name, arg_name))

for method_name, (query_name, mapping) in LIST_QUERIES.items():
    setattr(ThothClient1_0_0, method_name, _list_method(query_name, mapping))

for method_name, (query_name, mapping) in COUNT_QUERIES.items():
    setattr(ThothClient1_0_0, method_name, _count_method(query_name, mapping))

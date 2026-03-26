#!/usr/bin/env python3
"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""

import json
import re
import urllib

from .errors import GraphQLError, ResponseEmptyError, ThothError


def _fields(field_names, quoted_fields):
    return [(field_name, field_name in quoted_fields)
            for field_name in field_names]


def _data_spec(field_names, quoted_fields, return_value):
    return {
        "data_fields": _fields(field_names, quoted_fields),
        "return_value": return_value,
    }


def _flat_spec(field_names, quoted_fields, return_value):
    return {
        "flat_fields": _fields(field_names, quoted_fields),
        "return_value": return_value,
    }


def _markup_data_spec(field_names, quoted_fields, return_value):
    spec = _data_spec(field_names, quoted_fields, return_value)
    spec["extra_args"] = [("markupFormat", False)]
    return spec


def _upload_spec(field_names, quoted_fields, return_fields):
    return {
        "data_fields": _fields(field_names, quoted_fields),
        "return_fields": return_fields,
    }


NEW_PUBLISHER = [
    "publisherName", "publisherShortname", "publisherUrl", "zitadelId",
    "accessibilityStatement", "accessibilityReportUrl",
]
NEW_IMPRINT = [
    "publisherId", "imprintName", "imprintUrl", "crossmarkDoi", "s3Bucket",
    "cdnDomain", "cloudfrontDistId", "defaultCurrency", "defaultPlace",
    "defaultLocale",
]
NEW_WORK = [
    "workType", "workStatus", "reference", "edition", "imprintId", "doi",
    "publicationDate", "withdrawnDate", "place", "pageCount",
    "pageBreakdown", "imageCount", "tableCount", "audioCount", "videoCount",
    "license", "copyrightHolder", "landingPage", "lccn", "oclc",
    "generalNote", "bibliographyNote", "toc", "resourcesDescription",
    "coverUrl", "coverCaption", "firstPage", "lastPage", "pageInterval",
]
NEW_PUBLICATION = [
    "publicationType", "workId", "isbn", "widthMm", "widthIn", "heightMm",
    "heightIn", "depthMm", "depthIn", "weightG", "weightOz",
    "accessibilityStandard", "accessibilityAdditionalStandard",
    "accessibilityException", "accessibilityReportUrl",
]
NEW_PRICE = ["publicationId", "currencyCode", "unitPrice"]
NEW_LANGUAGE = ["workId", "languageCode", "languageRelation"]
NEW_SUBJECT = ["workId", "subjectType", "subjectCode", "subjectOrdinal"]
NEW_SERIES = [
    "seriesType", "seriesName", "issnPrint", "issnDigital", "seriesUrl",
    "seriesDescription", "seriesCfpUrl", "imprintId",
]
NEW_ISSUE = ["seriesId", "workId", "issueOrdinal", "issueNumber"]
NEW_CONTRIBUTOR = ["firstName", "lastName", "fullName", "orcid", "website"]
NEW_CONTRIBUTION = [
    "workId", "contributorId", "contributionType", "mainContribution",
    "firstName", "lastName", "fullName", "contributionOrdinal",
]
NEW_AFFILIATION = [
    "contributionId", "institutionId", "affiliationOrdinal", "position",
]
NEW_INSTITUTION = ["institutionName", "institutionDoi", "ror", "countryCode"]
NEW_LOCATION = [
    "publicationId", "landingPage", "fullTextUrl", "locationPlatform",
    "canonical",
]
NEW_FUNDING = [
    "workId", "institutionId", "program", "projectName", "projectShortname",
    "grantNumber",
]
NEW_WORK_RELATION = [
    "relatorWorkId", "relatedWorkId", "relationType", "relationOrdinal",
]
NEW_REFERENCE = [
    "workId", "referenceOrdinal", "doi", "unstructuredCitation", "issn",
    "isbn", "journalTitle", "articleTitle", "seriesTitle", "volumeTitle",
    "edition", "author", "volume", "issue", "firstPage", "componentNumber",
    "standardDesignator", "standardsBodyName", "standardsBodyAcronym", "url",
    "publicationDate", "retrievalDate",
]
NEW_TITLE = ["workId", "localeCode", "fullTitle", "title", "subtitle",
             "canonical"]
NEW_ABSTRACT = ["workId", "content", "localeCode", "abstractType",
                "canonical"]
NEW_BIOGRAPHY = ["contributionId", "content", "canonical", "localeCode"]
NEW_ADDITIONAL_RESOURCE = [
    "workId", "title", "description", "attribution", "resourceType", "doi",
    "handle", "url", "date", "resourceOrdinal",
]
NEW_AWARD = [
    "workId", "title", "url", "category", "year", "jury", "country",
    "prizeStatement", "role", "awardOrdinal",
]
NEW_ENDORSEMENT = [
    "workId", "authorName", "authorRole", "authorOrcid",
    "authorInstitutionId", "url", "text", "endorsementOrdinal",
]
NEW_BOOK_REVIEW = [
    "workId", "title", "authorName", "reviewerOrcid",
    "reviewerInstitutionId", "url", "doi", "reviewDate", "journalName",
    "journalVolume", "journalNumber", "journalIssn", "pageRange", "text",
    "reviewOrdinal",
]
NEW_WORK_FEATURED_VIDEO = ["workId", "title", "url", "width", "height"]
NEW_CONTACT = ["publisherId", "contactType", "email"]

PATCH_PUBLISHER = ["publisherId"] + NEW_PUBLISHER
PATCH_IMPRINT = ["imprintId"] + NEW_IMPRINT
PATCH_WORK = ["workId"] + NEW_WORK
PATCH_PUBLICATION = ["publicationId"] + NEW_PUBLICATION
PATCH_PRICE = ["priceId"] + NEW_PRICE
PATCH_LANGUAGE = ["languageId"] + NEW_LANGUAGE
PATCH_SUBJECT = ["subjectId"] + NEW_SUBJECT
PATCH_SERIES = ["seriesId"] + NEW_SERIES
PATCH_ISSUE = ["issueId"] + NEW_ISSUE
PATCH_CONTRIBUTOR = ["contributorId"] + NEW_CONTRIBUTOR
PATCH_CONTRIBUTION = ["contributionId"] + NEW_CONTRIBUTION
PATCH_AFFILIATION = ["affiliationId"] + NEW_AFFILIATION
PATCH_INSTITUTION = ["institutionId"] + NEW_INSTITUTION
PATCH_LOCATION = ["locationId"] + NEW_LOCATION
PATCH_FUNDING = ["fundingId"] + NEW_FUNDING
PATCH_WORK_RELATION = ["workRelationId"] + NEW_WORK_RELATION
PATCH_REFERENCE = ["referenceId"] + NEW_REFERENCE
PATCH_TITLE = ["titleId"] + NEW_TITLE
PATCH_ABSTRACT = ["abstractId"] + NEW_ABSTRACT
PATCH_BIOGRAPHY = ["biographyId"] + NEW_BIOGRAPHY
PATCH_ADDITIONAL_RESOURCE = ["additionalResourceId"] + NEW_ADDITIONAL_RESOURCE
PATCH_AWARD = ["awardId"] + NEW_AWARD
PATCH_ENDORSEMENT = ["endorsementId"] + NEW_ENDORSEMENT
PATCH_BOOK_REVIEW = ["bookReviewId"] + NEW_BOOK_REVIEW
PATCH_WORK_FEATURED_VIDEO = ["workFeaturedVideoId"] + NEW_WORK_FEATURED_VIDEO
PATCH_CONTACT = ["contactId"] + NEW_CONTACT

QUOTED_PUBLISHER = set(NEW_PUBLISHER)
QUOTED_IMPRINT = {
    "publisherId", "imprintName", "imprintUrl", "crossmarkDoi", "s3Bucket",
    "cdnDomain", "cloudfrontDistId", "defaultPlace",
}
QUOTED_WORK = {
    "reference", "imprintId", "doi", "publicationDate", "withdrawnDate",
    "place", "pageBreakdown", "license", "copyrightHolder", "landingPage",
    "lccn", "oclc", "generalNote", "bibliographyNote", "toc",
    "resourcesDescription", "coverUrl", "coverCaption", "firstPage",
    "lastPage", "pageInterval",
}
QUOTED_PUBLICATION = {"workId", "isbn", "accessibilityReportUrl"}
QUOTED_PRICE = {"publicationId"}
QUOTED_LANGUAGE = {"workId"}
QUOTED_SUBJECT = {"workId", "subjectCode"}
QUOTED_SERIES = {
    "seriesName", "issnPrint", "issnDigital", "seriesUrl",
    "seriesDescription", "seriesCfpUrl", "imprintId",
}
QUOTED_ISSUE = {"seriesId", "workId"}
QUOTED_CONTRIBUTOR = set(NEW_CONTRIBUTOR)
QUOTED_CONTRIBUTION = {
    "workId", "contributorId", "firstName", "lastName", "fullName",
}
QUOTED_AFFILIATION = {"contributionId", "institutionId", "position"}
QUOTED_INSTITUTION = {"institutionName", "institutionDoi", "ror"}
QUOTED_LOCATION = {"publicationId", "landingPage", "fullTextUrl"}
QUOTED_FUNDING = {
    "workId", "institutionId", "program", "projectName", "projectShortname",
    "grantNumber",
}
QUOTED_WORK_RELATION = {"relatorWorkId", "relatedWorkId"}
QUOTED_REFERENCE = {
    "workId", "doi", "unstructuredCitation", "issn", "isbn", "journalTitle",
    "articleTitle", "seriesTitle", "volumeTitle", "author", "volume",
    "issue", "firstPage", "componentNumber", "standardDesignator",
    "standardsBodyName", "standardsBodyAcronym", "url", "publicationDate",
    "retrievalDate",
}
QUOTED_TITLE = {"workId", "fullTitle", "title", "subtitle"}
QUOTED_ABSTRACT = {"workId", "content"}
QUOTED_BIOGRAPHY = {"contributionId", "content"}
QUOTED_ADDITIONAL_RESOURCE = {
    "workId", "title", "description", "attribution", "doi", "handle", "url",
    "date",
}
QUOTED_AWARD = {"workId", "title", "url", "category", "year", "jury",
                "prizeStatement"}
QUOTED_ENDORSEMENT = {
    "workId", "authorName", "authorRole", "authorOrcid",
    "authorInstitutionId", "url", "text",
}
QUOTED_BOOK_REVIEW = {
    "workId", "title", "authorName", "reviewerOrcid",
    "reviewerInstitutionId", "url", "doi", "reviewDate", "journalName",
    "journalVolume", "journalNumber", "journalIssn", "pageRange", "text",
}
QUOTED_WORK_FEATURED_VIDEO = {"workId", "title", "url"}
QUOTED_CONTACT = {"publisherId", "email"}
QUOTED_UPLOAD = {
    "publicationId", "workId", "additionalResourceId", "workFeaturedVideoId",
    "declaredMimeType", "declaredExtension", "declaredSha256", "fileUploadId",
}

FILE_FIELDS = [
    "fileId",
    "fileType",
    "workId",
    "publicationId",
    "additionalResourceId",
    "workFeaturedVideoId",
    "objectKey",
    "cdnUrl",
    "mimeType",
    "bytes",
    "sha256",
    "createdAt",
    "updatedAt",
]
FILE_UPLOAD_RESPONSE_FIELDS = [
    "fileUploadId",
    "uploadUrl",
    "uploadHeaders { name value }",
    "expiresAt",
]


class ThothMutation:
    """GraphQL mutation in Thoth."""

    MUTATIONS = {
        "createPublisher": _data_spec(NEW_PUBLISHER, QUOTED_PUBLISHER,
                                       "publisherId"),
        "createImprint": _data_spec(NEW_IMPRINT, QUOTED_IMPRINT, "imprintId"),
        "createWork": _data_spec(NEW_WORK, QUOTED_WORK, "workId"),
        "createPublication": _data_spec(NEW_PUBLICATION, QUOTED_PUBLICATION,
                                         "publicationId"),
        "createPrice": _data_spec(NEW_PRICE, QUOTED_PRICE, "priceId"),
        "createLanguage": _data_spec(NEW_LANGUAGE, QUOTED_LANGUAGE,
                                      "languageId"),
        "createSubject": _data_spec(NEW_SUBJECT, QUOTED_SUBJECT, "subjectId"),
        "createSeries": _data_spec(NEW_SERIES, QUOTED_SERIES, "seriesId"),
        "createIssue": _data_spec(NEW_ISSUE, QUOTED_ISSUE, "issueId"),
        "createContributor": _data_spec(NEW_CONTRIBUTOR, QUOTED_CONTRIBUTOR,
                                         "contributorId"),
        "createContribution": _data_spec(NEW_CONTRIBUTION,
                                          QUOTED_CONTRIBUTION,
                                          "contributionId"),
        "createAffiliation": _data_spec(NEW_AFFILIATION, QUOTED_AFFILIATION,
                                         "affiliationId"),
        "createInstitution": _data_spec(NEW_INSTITUTION, QUOTED_INSTITUTION,
                                         "institutionId"),
        "createLocation": _data_spec(NEW_LOCATION, QUOTED_LOCATION,
                                      "locationId"),
        "createFunding": _data_spec(NEW_FUNDING, QUOTED_FUNDING, "fundingId"),
        "createWorkRelation": _data_spec(NEW_WORK_RELATION,
                                          QUOTED_WORK_RELATION,
                                          "workRelationId"),
        "createReference": _data_spec(NEW_REFERENCE, QUOTED_REFERENCE,
                                       "referenceId"),
        "createTitle": _markup_data_spec(NEW_TITLE, QUOTED_TITLE, "titleId"),
        "createAbstract": _markup_data_spec(NEW_ABSTRACT, QUOTED_ABSTRACT,
                                             "abstractId"),
        "createBiography": _markup_data_spec(NEW_BIOGRAPHY, QUOTED_BIOGRAPHY,
                                              "biographyId"),
        "createAdditionalResource": _markup_data_spec(
            NEW_ADDITIONAL_RESOURCE, QUOTED_ADDITIONAL_RESOURCE,
            "workResourceId"
        ),
        "createAward": _markup_data_spec(NEW_AWARD, QUOTED_AWARD, "awardId"),
        "createEndorsement": _markup_data_spec(NEW_ENDORSEMENT,
                                                QUOTED_ENDORSEMENT,
                                                "endorsementId"),
        "createBookReview": _markup_data_spec(NEW_BOOK_REVIEW,
                                               QUOTED_BOOK_REVIEW,
                                               "bookReviewId"),
        "createWorkFeaturedVideo": _data_spec(NEW_WORK_FEATURED_VIDEO,
                                               QUOTED_WORK_FEATURED_VIDEO,
                                               "workFeaturedVideoId"),
        "createContact": _data_spec(NEW_CONTACT, QUOTED_CONTACT, "contactId"),
        "updatePublisher": _data_spec(PATCH_PUBLISHER,
                                       QUOTED_PUBLISHER | {"publisherId"},
                                       "publisherId"),
        "updateImprint": _data_spec(PATCH_IMPRINT,
                                     QUOTED_IMPRINT | {"imprintId"},
                                     "imprintId"),
        "updateWork": _data_spec(PATCH_WORK, QUOTED_WORK | {"workId"},
                                  "workId"),
        "updatePublication": _data_spec(
            PATCH_PUBLICATION, QUOTED_PUBLICATION | {"publicationId"},
            "publicationId"
        ),
        "updatePrice": _data_spec(PATCH_PRICE, QUOTED_PRICE | {"priceId"},
                                   "priceId"),
        "updateLanguage": _data_spec(PATCH_LANGUAGE,
                                      QUOTED_LANGUAGE | {"languageId"},
                                      "languageId"),
        "updateSubject": _data_spec(PATCH_SUBJECT,
                                     QUOTED_SUBJECT | {"subjectId"},
                                     "subjectId"),
        "updateSeries": _data_spec(PATCH_SERIES,
                                    QUOTED_SERIES | {"seriesId"},
                                    "seriesId"),
        "updateIssue": _data_spec(PATCH_ISSUE, QUOTED_ISSUE | {"issueId"},
                                   "issueId"),
        "updateContributor": _data_spec(
            PATCH_CONTRIBUTOR, QUOTED_CONTRIBUTOR | {"contributorId"},
            "contributorId"
        ),
        "updateContribution": _data_spec(
            PATCH_CONTRIBUTION, QUOTED_CONTRIBUTION | {"contributionId"},
            "contributionId"
        ),
        "updateAffiliation": _data_spec(
            PATCH_AFFILIATION, QUOTED_AFFILIATION | {"affiliationId"},
            "affiliationId"
        ),
        "updateInstitution": _data_spec(
            PATCH_INSTITUTION, QUOTED_INSTITUTION | {"institutionId"},
            "institutionId"
        ),
        "updateLocation": _data_spec(PATCH_LOCATION,
                                      QUOTED_LOCATION | {"locationId"},
                                      "locationId"),
        "updateFunding": _data_spec(PATCH_FUNDING,
                                     QUOTED_FUNDING | {"fundingId"},
                                     "fundingId"),
        "updateWorkRelation": _data_spec(
            PATCH_WORK_RELATION, QUOTED_WORK_RELATION | {"workRelationId"},
            "workRelationId"
        ),
        "updateReference": _data_spec(
            PATCH_REFERENCE, QUOTED_REFERENCE | {"referenceId"},
            "referenceId"
        ),
        "updateTitle": _markup_data_spec(PATCH_TITLE,
                                          QUOTED_TITLE | {"titleId"},
                                          "titleId"),
        "updateAbstract": _markup_data_spec(PATCH_ABSTRACT,
                                             QUOTED_ABSTRACT | {"abstractId"},
                                             "abstractId"),
        "updateBiography": _markup_data_spec(
            PATCH_BIOGRAPHY, QUOTED_BIOGRAPHY | {"biographyId"},
            "biographyId"
        ),
        "updateAdditionalResource": _markup_data_spec(
            PATCH_ADDITIONAL_RESOURCE,
            QUOTED_ADDITIONAL_RESOURCE | {"additionalResourceId"},
            "workResourceId"
        ),
        "updateAward": _markup_data_spec(PATCH_AWARD,
                                          QUOTED_AWARD | {"awardId"},
                                          "awardId"),
        "updateEndorsement": _markup_data_spec(
            PATCH_ENDORSEMENT, QUOTED_ENDORSEMENT | {"endorsementId"},
            "endorsementId"
        ),
        "updateBookReview": _markup_data_spec(
            PATCH_BOOK_REVIEW, QUOTED_BOOK_REVIEW | {"bookReviewId"},
            "bookReviewId"
        ),
        "updateWorkFeaturedVideo": _data_spec(
            PATCH_WORK_FEATURED_VIDEO,
            QUOTED_WORK_FEATURED_VIDEO | {"workFeaturedVideoId"},
            "workFeaturedVideoId"
        ),
        "updateContact": _data_spec(PATCH_CONTACT,
                                     QUOTED_CONTACT | {"contactId"},
                                     "contactId"),
        "deleteWork": _flat_spec(["workId"], {"workId"}, "workId"),
        "deletePublisher": _flat_spec(["publisherId"], {"publisherId"},
                                       "publisherId"),
        "deleteImprint": _flat_spec(["imprintId"], {"imprintId"},
                                     "imprintId"),
        "deleteContributor": _flat_spec(["contributorId"], {"contributorId"},
                                         "contributorId"),
        "deleteContribution": _flat_spec(["contributionId"],
                                          {"contributionId"},
                                          "contributionId"),
        "deletePublication": _flat_spec(["publicationId"], {"publicationId"},
                                         "publicationId"),
        "deleteSeries": _flat_spec(["seriesId"], {"seriesId"}, "seriesId"),
        "deleteIssue": _flat_spec(["issueId"], {"issueId"}, "issueId"),
        "deleteLanguage": _flat_spec(["languageId"], {"languageId"},
                                      "languageId"),
        "deleteTitle": _flat_spec(["titleId"], {"titleId"}, "titleId"),
        "deleteInstitution": _flat_spec(["institutionId"], {"institutionId"},
                                         "institutionId"),
        "deleteFunding": _flat_spec(["fundingId"], {"fundingId"},
                                     "fundingId"),
        "deleteLocation": _flat_spec(["locationId"], {"locationId"},
                                      "locationId"),
        "deletePrice": _flat_spec(["priceId"], {"priceId"}, "priceId"),
        "deleteSubject": _flat_spec(["subjectId"], {"subjectId"}, "subjectId"),
        "deleteAffiliation": _flat_spec(["affiliationId"], {"affiliationId"},
                                         "affiliationId"),
        "deleteWorkRelation": _flat_spec(["workRelationId"],
                                          {"workRelationId"},
                                          "workRelationId"),
        "deleteReference": _flat_spec(["referenceId"], {"referenceId"},
                                       "referenceId"),
        "deleteAdditionalResource": _flat_spec(["additionalResourceId"],
                                                {"additionalResourceId"},
                                                "workResourceId"),
        "deleteAward": _flat_spec(["awardId"], {"awardId"}, "awardId"),
        "deleteEndorsement": _flat_spec(["endorsementId"], {"endorsementId"},
                                         "endorsementId"),
        "deleteBookReview": _flat_spec(["bookReviewId"], {"bookReviewId"},
                                        "bookReviewId"),
        "deleteWorkFeaturedVideo": _flat_spec(
            ["workFeaturedVideoId"], {"workFeaturedVideoId"},
            "workFeaturedVideoId"
        ),
        "deleteAbstract": _flat_spec(["abstractId"], {"abstractId"},
                                      "abstractId"),
        "deleteBiography": _flat_spec(["biographyId"], {"biographyId"},
                                       "biographyId"),
        "deleteContact": _flat_spec(["contactId"], {"contactId"},
                                     "contactId"),
        "moveAffiliation": _flat_spec(["affiliationId", "newOrdinal"],
                                       {"affiliationId"}, "affiliationId"),
        "moveContribution": _flat_spec(["contributionId", "newOrdinal"],
                                        {"contributionId"},
                                        "contributionId"),
        "moveIssue": _flat_spec(["issueId", "newOrdinal"], {"issueId"},
                                 "issueId"),
        "moveReference": _flat_spec(["referenceId", "newOrdinal"],
                                     {"referenceId"}, "referenceId"),
        "moveAdditionalResource": _flat_spec(
            ["additionalResourceId", "newOrdinal"], {"additionalResourceId"},
            "workResourceId"
        ),
        "moveAward": _flat_spec(["awardId", "newOrdinal"], {"awardId"},
                                 "awardId"),
        "moveEndorsement": _flat_spec(["endorsementId", "newOrdinal"],
                                       {"endorsementId"},
                                       "endorsementId"),
        "moveBookReview": _flat_spec(["bookReviewId", "newOrdinal"],
                                      {"bookReviewId"}, "bookReviewId"),
        "moveSubject": _flat_spec(["subjectId", "newOrdinal"], {"subjectId"},
                                   "subjectId"),
        "moveWorkRelation": _flat_spec(["workRelationId", "newOrdinal"],
                                        {"workRelationId"},
                                        "workRelationId"),
        "initPublicationFileUpload": _upload_spec(
            ["publicationId", "declaredMimeType", "declaredExtension",
             "declaredSha256"],
            QUOTED_UPLOAD, FILE_UPLOAD_RESPONSE_FIELDS
        ),
        "initFrontcoverFileUpload": _upload_spec(
            ["workId", "declaredMimeType", "declaredExtension",
             "declaredSha256"],
            QUOTED_UPLOAD, FILE_UPLOAD_RESPONSE_FIELDS
        ),
        "initAdditionalResourceFileUpload": _upload_spec(
            ["additionalResourceId", "declaredMimeType", "declaredExtension",
             "declaredSha256"],
            QUOTED_UPLOAD, FILE_UPLOAD_RESPONSE_FIELDS
        ),
        "initWorkFeaturedVideoFileUpload": _upload_spec(
            ["workFeaturedVideoId", "declaredMimeType", "declaredExtension",
             "declaredSha256"],
            QUOTED_UPLOAD, FILE_UPLOAD_RESPONSE_FIELDS
        ),
        "completeFileUpload": _upload_spec(
            ["fileUploadId"], QUOTED_UPLOAD, FILE_FIELDS
        ),
    }

    def __init__(self, mutation_name, mutation_data, nested=True,
                 extra_args=None):
        self.mutation_name = mutation_name
        self.mutation_data = mutation_data or {}
        self.extra_args = extra_args or {}
        self.spec = self.MUTATIONS[mutation_name]
        self.request = self.prepare_request(nested)

    def prepare_request(self, nested):
        """Format the mutation request string."""
        arguments = []

        for field_name, enclose in self.spec.get("extra_args", []):
            if field_name in self.extra_args and self.extra_args[field_name]:
                arguments.append(self._statement(field_name,
                                                 self.extra_args[field_name],
                                                 enclose))

        if "data_fields" in self.spec:
            data_str = self.generate_values(self.spec["data_fields"],
                                            self.mutation_data)
            arguments.append("data: {\n%s\n}" % data_str if data_str else
                             "data: {}")
        else:
            arguments.append(self.generate_values(self.spec["flat_fields"],
                                                  self.mutation_data))

        arguments_str = ",\n".join([part for part in arguments if part])
        return_fields = self.prepare_return_fields()

        if return_fields:
            payload = """
                mutation {
                    %(mutation_name)s(
                        %(arguments)s
                    ) {
                        %(return_fields)s
                    }
                }
            """
        else:
            payload = """
                mutation {
                    %(mutation_name)s(
                        %(arguments)s
                    )
                }
            """

        return payload % {
            "mutation_name": self.mutation_name,
            "arguments": arguments_str,
            "return_fields": return_fields,
        }

    def prepare_return_fields(self):
        if "return_fields" in self.spec:
            return "\n".join(self.spec["return_fields"])
        return self.spec.get("return_value", "")

    def run(self, client):
        """Perform the GraphQL mutation and report any errors."""
        result = ""
        try:
            result = client.execute(self.request)
            if result == "":
                raise ResponseEmptyError(self.request, "None")
            serialised = json.loads(result)
            if "errors" in serialised:
                raise GraphQLError(self.request, result)

            response = serialised["data"][self.mutation_name]
            if "return_fields" in self.spec:
                return response
            return response[self.spec["return_value"]]
        except (KeyError, TypeError, ValueError, json.decoder.JSONDecodeError,
                urllib.error.HTTPError) as error:
            if result == "":
                result = error
            raise ThothError(self.request, result)

    @staticmethod
    def _statement(key, value, enclose):
        if value is None or str(value) == "":
            return ""
        if enclose:
            return '{}: "{}"'.format(key, ThothMutation.sanitise(value))
        return "{}: {}".format(key, value)

    @staticmethod
    def sanitise(text):
        """Escape quotes and linebreaks."""
        tmp = re.sub(r'(\r\n?|\n)', r'\\n', str(text))
        return tmp.replace('"', '\\"')

    def generate_values(self, fields, source):
        """Returns mutation statements based on object attributes."""
        values = []
        for key, enclose in fields:
            if key not in source:
                continue
            statement = self._statement(key, source.get(key), enclose)
            if statement:
                values.append(statement)
        return "\n".join(values)

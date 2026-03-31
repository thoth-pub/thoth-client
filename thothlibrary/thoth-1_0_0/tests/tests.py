"""
Copyright (c) 2026 Thoth Open Metadata
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json
import unittest

import requests_mock

from thothlibrary import ThothClient
from thothlibrary.client import THOTH_VERSION


class Thoth100Tests(unittest.TestCase):
    def setUp(self):
        self.endpoint = "https://api.test100.thoth.pub"
        self.graphql_endpoint = "{}/graphql".format(self.endpoint)
        self.version = "1.0.0"

    def _client(self):
        return ThothClient(version=self.version, thoth_endpoint=self.endpoint)

    @staticmethod
    def _query_text(mocker):
        return json.loads(mocker.last_request.text)["query"]

    def test_default_version_is_v1(self):
        self.assertEqual(THOTH_VERSION, "1.0.0")

    def test_work_query_uses_multilingual_fields(self):
        payload = {
            "data": {
                "work": {
                    "workId": "work-1",
                    "publicationDate": "2024-01-02",
                    "place": "London",
                    "titles": [{
                        "titleId": "title-1",
                        "localeCode": "EN",
                        "fullTitle": "Canonical Title",
                        "title": "Canonical Title",
                        "subtitle": None,
                        "canonical": True,
                        "__typename": "Title",
                    }],
                    "abstracts": [{
                        "abstractId": "abstract-1",
                        "localeCode": "EN",
                        "content": "Short abstract",
                        "abstractType": "LONG",
                        "canonical": True,
                        "__typename": "Abstract",
                    }],
                    "contributions": [{
                        "contributionId": "contribution-1",
                        "contributionType": "AUTHOR",
                        "fullName": "Jane Doe",
                        "contributionOrdinal": 1,
                        "__typename": "Contribution",
                    }],
                    "imprint": {
                        "publisher": {
                            "publisherName": "Open Book Publishers",
                            "publisherId": "publisher-1",
                            "__typename": "Publisher",
                        },
                        "__typename": "Imprint",
                    },
                    "__typename": "Work",
                }
            }
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            result = self._client().work_by_id(work_id="work-1")
            query = self._query_text(mocker)

        self.assertIn("titles(order:", query)
        self.assertIn("abstracts(order:", query)
        self.assertNotIn("\n                shortAbstract", query)
        self.assertNotIn("\n                longAbstract", query)
        self.assertNotIn("\n                biography", query)
        self.assertIn("Canonical Title", str(result))

    def test_publication_query_includes_file_and_accessibility(self):
        payload = {
            "data": {
                "publication": {
                    "publicationId": "publication-1",
                    "publicationType": "PDF",
                    "workId": "work-1",
                    "isbn": "9780000000001",
                    "accessibilityStandard": "WCAG_AA",
                    "accessibilityAdditionalStandard": None,
                    "accessibilityException": None,
                    "accessibilityReportUrl": "https://example.com/report",
                    "prices": [],
                    "locations": [],
                    "file": {
                        "fileId": "file-1",
                        "fileType": "PUBLICATION",
                        "cdnUrl": "https://cdn.example/file.pdf",
                        "__typename": "File",
                    },
                    "work": {
                        "workId": "work-1",
                        "publicationDate": "2024-01-02",
                        "place": "London",
                        "titles": [{
                            "titleId": "title-1",
                            "localeCode": "EN",
                            "fullTitle": "Canonical Title",
                            "title": "Canonical Title",
                            "subtitle": None,
                            "canonical": True,
                            "__typename": "Title",
                        }],
                        "contributions": [],
                        "imprint": {
                            "publisher": {
                                "publisherName": "OBP",
                                "publisherId": "publisher-1",
                                "__typename": "Publisher",
                            },
                            "__typename": "Imprint",
                        },
                        "__typename": "Work",
                    },
                    "__typename": "Publication",
                }
            }
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            self._client().publication(publication_id="publication-1")
            query = self._query_text(mocker)

        self.assertIn("file {", query)
        self.assertIn("accessibilityStandard", query)
        self.assertIn("accessibilityReportUrl", query)

    def test_title_query_accepts_markup_format(self):
        payload = {
            "data": {
                "title": {
                    "titleId": "title-1",
                    "workId": "work-1",
                    "localeCode": "EN",
                    "fullTitle": "Canonical Title",
                    "title": "Canonical Title",
                    "subtitle": None,
                    "canonical": True,
                    "work": {
                        "workId": "work-1",
                        "titles": [{
                            "titleId": "title-1",
                            "localeCode": "EN",
                            "fullTitle": "Canonical Title",
                            "title": "Canonical Title",
                            "subtitle": None,
                            "canonical": True,
                            "__typename": "Title",
                        }],
                        "__typename": "Work",
                    },
                    "__typename": "Title",
                }
            }
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            self._client().title(title_id="title-1", markup_format="HTML")
            query = self._query_text(mocker)

        self.assertIn("markupFormat: HTML", query)

    def test_book_ids_wraps_books_query(self):
        payload = {
            "data": {
                "books": [{
                    "workId": "book-1",
                    "__typename": "Work",
                }]
            }
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            result = self._client().bookIds()
            query = self._query_text(mocker)

        self.assertIn("books(", query)
        self.assertEqual(result[0].workId, "book-1")

    def test_update_work_uses_v1_fields(self):
        payload = {"data": {"updateWork": {"workId": "work-1"}}}
        mutation_data = {
            "workId": "work-1",
            "workType": "MONOGRAPH",
            "workStatus": "ACTIVE",
            "imprintId": "imprint-1",
            "bibliographyNote": "Updated bibliography",
            "resourcesDescription": "Supplementary resources",
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            self._client().update_work(mutation_data)
            query = self._query_text(mocker)

        self.assertIn('bibliographyNote: "Updated bibliography"', query)
        self.assertIn('resourcesDescription: "Supplementary resources"', query)
        self.assertNotIn("fullTitle:", query)
        self.assertNotIn("shortAbstract:", query)
        self.assertNotIn("longAbstract:", query)

    def test_create_title_uses_markup_argument(self):
        payload = {"data": {"createTitle": {"titleId": "title-1"}}}
        title_data = {
            "workId": "work-1",
            "localeCode": "EN",
            "fullTitle": "Canonical Title",
            "title": "Canonical Title",
            "canonical": "true",
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            result = self._client().create_title(title_data,
                                                 markup_format="HTML")
            query = self._query_text(mocker)

        self.assertEqual(result, "title-1")
        self.assertIn("markupFormat: HTML", query)
        self.assertIn('fullTitle: "Canonical Title"', query)

    def test_init_publication_file_upload_returns_structured_object(self):
        payload = {
            "data": {
                "initPublicationFileUpload": {
                    "fileUploadId": "upload-1",
                    "uploadUrl": "https://uploads.example",
                    "uploadHeaders": [{"name": "x-test", "value": "1"}],
                    "expiresAt": "2025-01-01T00:00:00Z",
                }
            }
        }
        upload_data = {
            "publicationId": "publication-1",
            "declaredMimeType": "application/pdf",
            "declaredExtension": "pdf",
            "declaredSha256": "abc123",
        }

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            result = self._client().init_publication_file_upload(upload_data)

        self.assertEqual(result.fileUploadId, "upload-1")
        self.assertEqual(result.uploadHeaders[0].name, "x-test")

    def test_pat_auth_sets_bearer_header(self):
        payload = {"data": {"works": []}}

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            client = self._client()
            client.set_token("test-pat")
            client.works()

        self.assertEqual(
            mocker.last_request.headers.get("Authorization"),
            "Bearer test-pat",
        )

    def test_move_subject_uses_flat_arguments(self):
        payload = {"data": {"moveSubject": {"subjectId": "subject-1"}}}
        move_data = {"subjectId": "subject-1", "newOrdinal": 2}

        with requests_mock.Mocker() as mocker:
            mocker.post(self.graphql_endpoint, json=payload)
            self._client().move_subject(move_data)
            query = self._query_text(mocker)

        self.assertIn('subjectId: "subject-1"', query)
        self.assertIn("newOrdinal: 2", query)
        self.assertNotIn("data: {", query)

    def test_new_v1_methods_exist(self):
        client = self._client()
        for method_name in [
            "chapters",
            "chapter_by_doi",
            "affiliations",
            "additional_resources",
            "awards",
            "endorsements",
            "book_reviews",
            "work_featured_videos",
            "contacts",
            "create_abstract",
            "update_title",
            "delete_contact",
            "complete_file_upload",
        ]:
            self.assertTrue(hasattr(client, method_name), method_name)


if __name__ == "__main__":
    unittest.main()

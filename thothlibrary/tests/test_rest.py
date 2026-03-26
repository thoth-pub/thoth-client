"""
Tests for the retained Thoth export API client.
"""
import unittest

import requests_mock

from thothlibrary import ThothRESTClient


class ThothRESTClientTests(unittest.TestCase):
    def setUp(self):
        self.endpoint = "https://export.test.thoth.pub"
        self.client = ThothRESTClient(endpoint=self.endpoint)

    def test_formats(self):
        payload = [{"id": "onix_3.0::project_muse", "name": "Project MUSE"}]
        with requests_mock.Mocker() as mocker:
            mocker.get(self.endpoint + "/formats/", json=payload)
            result = self.client.formats()

        self.assertEqual(result[0].id, "onix_3.0::project_muse")
        self.assertEqual(str(result[0]), "onix_3.0::project_muse")

    def test_format(self):
        payload = {"id": "onix_3.0::project_muse", "name": "Project MUSE"}
        with requests_mock.Mocker() as mocker:
            mocker.get(self.endpoint + "/formats/onix_3.0::project_muse",
                       json=payload)
            result = self.client.format("onix_3.0::project_muse")

        self.assertEqual(result.name, "Project MUSE")

    def test_specifications(self):
        payload = [{"name": "ONIX 3.0", "id": "onix_3.0"}]
        with requests_mock.Mocker() as mocker:
            mocker.get(self.endpoint + "/specifications/", json=payload)
            result = self.client.specifications()

        self.assertEqual(result[0].name, "ONIX 3.0")
        self.assertEqual(str(result[0]), "ONIX 3.0")

    def test_specification(self):
        payload = {"name": "ONIX 3.0", "id": "onix_3.0"}
        with requests_mock.Mocker() as mocker:
            mocker.get(self.endpoint + "/specifications/onix_3.0", json=payload)
            result = self.client.specification("onix_3.0")

        self.assertEqual(result.id, "onix_3.0")

    def test_platforms(self):
        payload = [{"name": "Project MUSE", "id": "project_muse"}]
        with requests_mock.Mocker() as mocker:
            mocker.get(self.endpoint + "/platforms/", json=payload)
            result = self.client.platforms()

        self.assertEqual(result[0].id, "project_muse")
        self.assertEqual(str(result[0]), "Project MUSE")

    def test_platform(self):
        payload = {"name": "Project MUSE", "id": "project_muse"}
        with requests_mock.Mocker() as mocker:
            mocker.get(self.endpoint + "/platforms/project_muse", json=payload)
            result = self.client.platform("project_muse")

        self.assertEqual(result.name, "Project MUSE")

    def test_work(self):
        payload = "<xml>work</xml>"
        with requests_mock.Mocker() as mocker:
            mocker.get(
                self.endpoint + "/specifications/onix_3.0/work/work-1",
                text=payload,
            )
            result = self.client.work("onix_3.0", "work-1")

        self.assertEqual(result, payload)

    def test_works(self):
        payload = "<xml>publisher</xml>"
        with requests_mock.Mocker() as mocker:
            mocker.get(
                self.endpoint + "/specifications/onix_3.0/publisher/publisher-1",
                text=payload,
            )
            result = self.client.works("onix_3.0", "publisher-1")

        self.assertEqual(result, payload)


if __name__ == "__main__":
    unittest.main()

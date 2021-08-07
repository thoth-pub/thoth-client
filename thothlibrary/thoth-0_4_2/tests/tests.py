import unittest

import requests_mock
from thothlibrary import ThothClient


class Thoth042Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endpoint = "https://api.test042.thoth.pub"
        self.version = "0.4.2"

    def test_works_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works', m)

            response = thoth_client.works(raw=True)

            self.assertEqual(mock_response, response)

        return None

    def test_publications_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publications', m)

            response = thoth_client.publications(raw=True)

            self.assertEqual(mock_response, response)

        return None

    def test_publishers_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publishers', m)

            response = thoth_client.publishers(raw=True)

            self.assertEqual(mock_response, response)

        return None

    def test_contributions_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributions', m)

            response = thoth_client.contributions(raw=True)

            self.assertEqual(mock_response, response)

        return None

    def setup_mocker(self, endpoint, m):
        """
        Sets up a mocker object by reading a json fixture
        @param endpoint: the file to read in the fixtures dir (no extension)
        @param m: the requests Mocker object
        @return: the mock string
        """
        with open("fixtures/{0}.json".format(endpoint), "r") as input_file:
            mock_response = input_file.read()

        m.register_uri('POST', 'https://api.thoth.pub/graphql',
                       text=mock_response)

        thoth_client = ThothClient(version=self.version,
                                   thoth_endpoint=self.endpoint)

        return mock_response, thoth_client


if __name__ == '__main__':
    unittest.main()

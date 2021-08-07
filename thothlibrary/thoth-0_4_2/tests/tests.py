import json
import unittest
import pickle

import requests_mock
from thothlibrary import ThothClient


class Thoth042Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.endpoint = "https://api.test042.thoth.pub"
        self.version = "0.4.2"

    def test_works(self):
        """
        Tests that good input to works produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works', m)
            self.pickle_tester('works', thoth_client.works)
        return None

    def test_works_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works_bad', m)
            self.pickle_tester('works', thoth_client.works, negative=True)
        return None

    def test_works_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('works', m)
            self.raw_tester(mock_response, thoth_client.works)
        return None

    def test_publications_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publications', m)
            self.raw_tester(mock_response, thoth_client.publications)
        return None

    def test_publishers_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('publishers', m)
            self.raw_tester(mock_response, thoth_client.publishers)
        return None

    def test_contributions_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self.setup_mocker('contributions', m)
            self.raw_tester(mock_response, thoth_client.contributions)
        return None

    def raw_tester(self, mock_response, method_to_call):
        """
        An echo test that ensures the client returns accurate raw responses
        @param mock_response: the mock response
        @param method_to_call: the method to call
        @return: None or an assertion error
        """
        response = method_to_call(raw=True)
        self.assertEqual(mock_response, response,
                         'Raw response was not echoed back correctly.')

    def pickle_tester(self, pickle_name, endpoint, negative=False):
        with open("fixtures/{0}.pickle".format(pickle_name)
                , "rb") as pickle_file:
            loaded_response = json.load(pickle_file)
            response = json.loads(json.dumps(endpoint()))

            if not negative:
                self.assertEqual(loaded_response, response)
            else:
                self.assertNotEqual(loaded_response, response)

    def setup_mocker(self, endpoint, m):
        """
        Sets up a mocker object by reading a json fixture
        @param endpoint: the file to read in the fixtures dir (no extension)
        @param m: the requests Mocker object
        @return: the mock string
        """
        with open("fixtures/{0}.json".format(endpoint), "r") as input_file:
            mock_response = input_file.read()

        m.register_uri('POST', '{}/graphql'.format(self.endpoint),
                       text=mock_response)

        thoth_client = ThothClient(version=self.version,
                                   thoth_endpoint=self.endpoint)

        return mock_response, thoth_client


if __name__ == '__main__':
    unittest.main()

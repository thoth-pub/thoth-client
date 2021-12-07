"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import json
import os
import unittest

import requests_mock
from thothlibrary import ThothClient


class Thoth060Tests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # we set this fake endpoint to ensure that the tests are definitely
        # running against the local objects, rather than any remote server
        self.endpoint = "https://api.test060.thoth.pub"
        self.version = "0.6.0"

    def test_contribution(self):
        """
        Tests that good input to contribution produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contribution', m)
            self._pickle_tester('contribution',
                                lambda:
                                thoth_client.contribution(
                                    contribution_id='29e4f46b-851a-4d7b-bb41-'
                                                    'e6f305fc2b11'))
        return None

    def test_contribution_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contribution_bad',
                                                             m)
            self._pickle_tester('contribution',
                                lambda: thoth_client.contribution(
                                    contribution_id='29e4f46b-851a-4d7b-bb41-'
                                                    'e6f305fc2b11'),
                                negative=True)
        return None

    def test_contribution_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contribution', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.contribution(
                                 contribution_id='29e4f46b-851a-4d7b-bb41-'
                                                 'e6f305fc2b11',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_contributions(self):
        """
        Tests that good input to contributions produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributions', m)
            self._pickle_tester('contributions', thoth_client.contributions)
        return None

    def test_contributions_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker(
                'contributions_bad',
                m)
            self._pickle_tester('contributions', thoth_client.contributions,
                                negative=True)

    def test_contributions_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributions', m)
            self._raw_tester(mock_response, thoth_client.contributions)
        return None

    def test_contributor(self):
        """
        Tests that good input to contributor produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributor', m)
            self._pickle_tester('contributor',
                                lambda:
                                thoth_client.contributor(
                                    contributor_id='e8def8cf-0dfe-4da9-b7fa-'
                                                   'f77e7aec7524'))
        return None

    def test_contributor_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributor_bad',
                                                             m)
            self._pickle_tester('contributor',
                                lambda: thoth_client.contributor(
                                    contributor_id='e8def8cf-0dfe-4da9-b7fa-'
                                                   'f77e7aec7524'),
                                negative=True)
        return None

    def test_contributor_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributor', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.contributor(
                                 contributor_id='e8def8cf-0dfe-4da9-b7fa-'
                                                'f77e7aec7524',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_contributors(self):
        """
        Tests that good input to contributors produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributors', m)
            self._pickle_tester('contributors', thoth_client.contributors)
        return None

    def test_contributors_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributors_bad',
                                                             m)
            self._pickle_tester('contributors', thoth_client.contributors,
                                negative=True)

    def test_contributors_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('contributors', m)
            self._raw_tester(mock_response, thoth_client.contributors)
        return None

    def test_institution(self):
        """
        Tests that good input to institution produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('institution', m)
            self._pickle_tester('institution',
                                lambda:
                                thoth_client.institution(
                                    institution_id='194614ac-d189-4a74-8bf4-'
                                                   '74c0c9de4a81'))
        return None

    def test_institution_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('funder_bad', m)
            self._pickle_tester('institution',
                                lambda: thoth_client.institution(
                                    institution_id='194614ac-d189-4a74-8bf4-'
                                                   '74c0c9de4a81'),
                                negative=True)
        return None

    def test_institution_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('funder', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.institution(
                                 institution_id='194614ac-d189-4a74-8bf4-'
                                                '74c0c9de4a81',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_institutions(self):
        """
        Tests that good input to institutions produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('institutions', m)
            self._pickle_tester('institutions', thoth_client.institutions)
        return None

    def test_institutions_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('institutions_bad',
                                                             m)
            self._pickle_tester('institutions', thoth_client.institutions,
                                negative=True)

    def test_institutions_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('institutions', m)
            self._raw_tester(mock_response, thoth_client.institutions)
        return None

    def test_funding(self):
        """
        Tests that good input to funding produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('funding', m)
            self._pickle_tester('funding',
                                lambda:
                                thoth_client.funding(
                                    funding_id='5323d3e7-3ae9-4778-8464-'
                                               '9400fbbb959e]'))
        return None

    def test_funding_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('funding_bad', m)

            self._pickle_tester('funding',
                                lambda: thoth_client.funding(
                                    funding_id='5323d3e7-3ae9-4778-8464-'
                                               '9400fbbb959e]'),
                                negative=True)
        return None

    def test_funding_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('funding', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.funding(
                                 funding_id='5323d3e7-3ae9-4778-8464-'
                                            '9400fbbb959e]',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_fundings(self):
        """
        Tests that good input to fundings produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('fundings', m)
            self._pickle_tester('fundings', thoth_client.fundings)
        return None

    def test_fundings_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('fundings_bad', m)
            self._pickle_tester('fundings', thoth_client.fundings,
                                negative=True)

    def test_fundings_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('fundings', m)
            self._raw_tester(mock_response, thoth_client.fundings)
        return None

    def test_imprint(self):
        """
        Tests that good input to imprint produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('imprint', m)
            self._pickle_tester('imprint',
                                lambda:
                                thoth_client.imprint(
                                    imprint_id='78b0a283-9be3-4fed-a811-'
                                               'a7d4b9df7b25'))
        return None

    def test_imprint_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('imprint_bad', m)
            self._pickle_tester('imprint',
                                lambda: thoth_client.imprint(
                                    imprint_id='78b0a283-9be3-4fed-a811-'
                                               'a7d4b9df7b25'),
                                negative=True)
        return None

    def test_imprint_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('imprint', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.imprint(
                                 imprint_id='78b0a283-9be3-4fed-a811-'
                                            'a7d4b9df7b25',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_imprints(self):
        """
        Tests that good input to imprints produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('imprints', m)
            self._pickle_tester('imprints', thoth_client.imprints)
        return None

    def test_imprints_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('imprints_bad', m)
            self._pickle_tester('imprints', thoth_client.imprints,
                                negative=True)

    def test_imprints_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('imprints', m)
            self._raw_tester(mock_response, thoth_client.imprints)
        return None

    def test_issue(self):
        """
        Tests that good input to issue produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('issue', m)
            self._pickle_tester('issue',
                                lambda:
                                thoth_client.issue(
                                    issue_id='6bd31b4c-35a9-4177-8074-'
                                             'dab4896a4a3d'))
        return None

    def test_issue_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('issue_bad', m)
            self._pickle_tester('issue',
                                lambda: thoth_client.issue(
                                    issue_id='6bd31b4c-35a9-4177-8074-'
                                             'dab4896a4a3d'),
                                negative=True)
        return None

    def test_issue_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('issue', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.issue(
                                 issue_id='6bd31b4c-35a9-4177-8074-'
                                          'dab4896a4a3d',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_issues(self):
        """
        Tests that good input to issues produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('issues', m)
            self._pickle_tester('issues', thoth_client.issues)
        return None

    def test_issues_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('issues_bad', m)
            self._pickle_tester('issues', thoth_client.issues,
                                negative=True)

    def test_issues_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('issues', m)
            self._raw_tester(mock_response, thoth_client.issues)
        return None

    def test_language(self):
        """
        Tests that good input to language produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('language', m)
            self._pickle_tester('language',
                                lambda:
                                thoth_client.language(
                                    language_id='c19e68dd-c5a3-48f1-bd56-'
                                                '089ee732604c'))
        return None

    def test_language_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('language_bad', m)
            self._pickle_tester('language',
                                lambda: thoth_client.language(
                                    language_id='c19e68dd-c5a3-48f1-bd56-'
                                                '089ee732604c'),
                                negative=True)
        return None

    def test_language_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('language', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.language(
                                 language_id='c19e68dd-c5a3-48f1-bd56-'
                                             '089ee732604c',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_languages(self):
        """
        Tests that good input to languages produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('languages', m)
            self._pickle_tester('languages', thoth_client.languages)
        return None

    def test_languages_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('languages_bad',
                                                             m)
            self._pickle_tester('languages', thoth_client.languages,
                                negative=True)

    def test_languages_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('languages', m)
            self._raw_tester(mock_response, thoth_client.languages)
        return None

    def test_price(self):
        """
        Tests that good input to price produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('price', m)
            self._pickle_tester('price',
                                lambda:
                                thoth_client.price(
                                    price_id='818567dd-7d3a-4963-8704-'
                                             '3381b5432877'))
        return None

    def test_price_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('price_bad',
                                                             m)
            self._pickle_tester('price',
                                lambda: thoth_client.price(
                                    price_id='818567dd-7d3a-4963-8704-'
                                             '3381b5432877'),
                                negative=True)
        return None

    def test_price_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('price', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.price(
                                 price_id='818567dd-7d3a-4963-8704-'
                                          '3381b5432877',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_prices(self):
        """
        Tests that good input to prices produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('prices', m)
            self._pickle_tester('prices', thoth_client.prices)
        return None

    def test_prices_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('prices_bad', m)
            self._pickle_tester('prices', thoth_client.prices,
                                negative=True)

    def test_prices_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('prices', m)
            self._raw_tester(mock_response, thoth_client.prices)
        return None

    def test_publication(self):
        """
        Tests that good input to publication produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publication', m)
            self._pickle_tester('publication',
                                lambda:
                                thoth_client.publication(
                                    publication_id='34712b75'
                                                   '-dcdd'
                                                   '-408b'
                                                   '-8d0c'
                                                   '-cf29a35'
                                                   'be2e5'))
        return None

    def test_publication_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publication_bad',
                                                             m)
            self._pickle_tester('publication',
                                lambda: thoth_client.publication(
                                    publication_id='34712b75-dcdd-408b-8d0c-'
                                                   'cf29a35be2e5'),
                                negative=True)
        return None

    def test_publication_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publication', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.publication(
                                 publication_id='34712b75-dcdd-408b-8d0c'
                                                '-cf29a'
                                                '35be2e5',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_publications(self):
        """
        Tests that good input to publications produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publications', m)
            self._pickle_tester('publications', thoth_client.publications)
        return None

    def test_publications_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publications_bad',
                                                             m)
            self._pickle_tester('publications', thoth_client.publications,
                                negative=True)
        return None

    def test_publications_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publications', m)
            self._raw_tester(mock_response, thoth_client.publications)
        return None

    def test_publisher(self):
        """
        Tests that good input to publisher produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publisher', m)
            self._pickle_tester('publisher',
                                lambda:
                                thoth_client.publisher(
                                    publisher_id='85fd969a-a16c-480b-b641-'
                                                 'cb9adf979c3b'))
        return None

    def test_publisher_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publisher_bad', m)
            self._pickle_tester('publisher',
                                lambda: thoth_client.publisher(
                                    publisher_id='85fd969a-a16c-480b-b641-'
                                                 'cb9adf979c3b'),
                                negative=True)
        return None

    def test_publisher_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publisher', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.publisher(
                                 publisher_id='85fd969a-a16c-480b-b641-'
                                              'cb9adf979c3b',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_publishers(self):
        """
        Tests that good input to publishers produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publishers', m)
            self._pickle_tester('publishers', thoth_client.publishers)
        return None

    def test_publishers_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publishers_bad',
                                                             m)
            self._pickle_tester('publishers', thoth_client.publishers,
                                negative=True)

    def test_publishers_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('publishers', m)
            self._raw_tester(mock_response, thoth_client.publishers)
        return None

    def test_series(self):
        """
        Tests that good input to series produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('series', m)
            self._pickle_tester('series',
                                lambda:
                                thoth_client.series(
                                    series_id='d4b47a76-abff-4047-a3c7-'
                                              'd44d85ccf009'))
        return None

    def test_series_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('series_bad',
                                                             m)
            self._pickle_tester('series',
                                lambda: thoth_client.series(
                                    series_id='d4b47a76-abff-4047-a3c7-'
                                              'd44d85ccf009'),
                                negative=True)
        return None

    def test_series_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('series', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.series(
                                 series_id='d4b47a76-abff-4047-a3c7-'
                                           'd44d85ccf009',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_serieses(self):
        """
        Tests that good input to serieses produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('serieses', m)
            self._pickle_tester('serieses', thoth_client.serieses)
        return None

    def test_serieses_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('serieses_bad', m)
            self._pickle_tester('serieses', thoth_client.serieses,
                                negative=True)

    def test_serieses_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('serieses', m)
            self._raw_tester(mock_response, thoth_client.serieses)
        return None

    def test_subject(self):
        """
        Tests that good input to subject produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('subject', m)
            self._pickle_tester('subject',
                                lambda:
                                thoth_client.subject(
                                    subject_id='1291208f-fc43-47a4-a8e6-'
                                               'e132477ad57b'))
        return None

    def test_subject_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('subject_bad', m)
            self._pickle_tester('subject',
                                lambda: thoth_client.subject(
                                    subject_id='1291208f-fc43-47a4-a8e6-'
                                               'e132477ad57b'),
                                negative=True)
        return None

    def test_subject_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('subject', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.subject(
                                 subject_id='1291208f-fc43-47a4-a8e6-'
                                            'e132477ad57b',
                                 raw=True),
                             lambda_mode=True)
        return None

    def test_subjects(self):
        """
        Tests that good input to subjects produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('subjects', m)
            self._pickle_tester('subjects', thoth_client.subjects)
        return None

    def test_subjects_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('subjects_bad', m)
            self._pickle_tester('subjects', thoth_client.subjects,
                                negative=True)

    def test_subjects_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('subjects', m)
            self._raw_tester(mock_response, thoth_client.subjects)
        return None

    def test_work_by_doi(self):
        """
        Tests that good input to work_by_doi produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('workByDoi', m)
            self._pickle_tester('workByDoi',
                                lambda:
                                thoth_client.work_by_doi(doi='https://doi.org/'
                                                             '10.21983/P3.0314.'
                                                             '1.00'))
        return None

    def test_work_by_doi_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('workByDoi_bad', m)
            self._pickle_tester('work',
                                lambda: thoth_client.work_by_doi(doi='https://'
                                                                     'doi.org/1'
                                                                     '0.21983/P'
                                                                     '3.0314.1.'
                                                                     '00'),
                                negative=True)
        return None

    def test_work_by_doi_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('workByDoi', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.work_by_doi(doi='https://doi.'
                                                                  'org/10.21983'
                                                                  '/P3.0314.1.'
                                                                  '00',
                                                              raw=True),
                             lambda_mode=True)
        return None

    def test_work_by_id(self):
        """
        Tests that good input to work_by_id produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('work', m)
            self._pickle_tester('work',
                                lambda:
                                thoth_client.work_by_id(work_id='e0f748b2-984f-'
                                                                '45cc-8b9e-'
                                                                '13989c31dda4'))
        return None

    def test_work_by_id_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('work_bad', m)
            self._pickle_tester('work',
                                lambda: thoth_client.work_by_id(
                                    work_id='e0f748b2'
                                            '-'
                                            '984f-'
                                            '45cc-'
                                            '8b9e-'
                                            '13989c31'
                                            'dda4'),
                                negative=True)
        return None

    def test_work_by_id_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('work', m)
            self._raw_tester(mock_response,
                             lambda: thoth_client.work_by_id(work_id='e0f748b2'
                                                                     '-'
                                                                     '984f-'
                                                                     '45cc-'
                                                                     '8b9e-'
                                                                     '13989c31'
                                                                     'dda4',
                                                             raw=True),
                             lambda_mode=True)
        return None

    def test_works(self):
        """
        Tests that good input to works produces saved good output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('works', m)
            self._pickle_tester('works', thoth_client.works)
        return None

    def test_works_bad_input(self):
        """
        Tests that bad input produces bad output
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('works_bad', m)
            self._pickle_tester('works', thoth_client.works, negative=True)
        return None

    def test_works_raw(self):
        """
        A test to ensure valid passthrough of raw json
        @return: None if successful
        """
        with requests_mock.Mocker() as m:
            mock_response, thoth_client = self._setup_mocker('works', m)
            self._raw_tester(mock_response, thoth_client.works)
        return None

    def _raw_tester(self, mock_response, method_to_call, lambda_mode=False):
        """
        An echo test that ensures the client returns accurate raw responses
        @param lambda_mode: whether the passed function is a complete lambda
        @param mock_response: the mock response
        @param method_to_call: the method to call
        @return: None or an assertion
        """
        if not lambda_mode:
            response = method_to_call(raw=True)
        else:
            response = method_to_call()

        self.assertEqual(mock_response, response,
                         'Raw response was not echoed back correctly.')

    def _pickle_tester(self, pickle_name, endpoint, negative=False):
        """
        A test of a function's output against a stored pickle (JSON)
        @param pickle_name: the .pickle file in the fixtures directory
        @param endpoint: the method to call
        @param negative: whether to assert equal (True) or unequal (False)
        @return: None or an assertion
        """
        path = os.path.join("fixtures", "{0}.pickle".format(pickle_name))
        with open(path, "rb") as pickle_file:
            loaded_response = json.load(pickle_file)
            response = json.loads(json.dumps(endpoint()))

            if not negative:
                self.assertEqual(loaded_response, response)
            else:
                self.assertNotEqual(loaded_response, response)

    def _setup_mocker(self, endpoint, m):
        """
        Sets up a mocker object by reading a json fixture
        @param endpoint: the file to read in the fixtures dir (no extension)
        @param m: the requests Mocker object
        @return: the mock string, a Thoth client for this version
        """
        path = os.path.join("fixtures", "{0}.json".format(endpoint))
        with open(path, "r") as input_file:
            mock_response = input_file.read()

        m.register_uri('POST', '{}/graphql'.format(self.endpoint),
                       text=mock_response)

        thoth_client = ThothClient(version=self.version,
                                   thoth_endpoint=self.endpoint)

        return mock_response, thoth_client


if __name__ == '__main__':
    unittest.main()

"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020 and (c) ΔQ Programming LLP, July 2021
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import importlib
import pkgutil

import thothlibrary
from .auth import ThothAuthenticator
from .graphql import GraphQLClientRequests as GraphQLClient
from .mutation import ThothMutation
from .query import ThothQuery
import re


class ThothClient:
    """Client to Thoth's GraphQL API"""

    def __init__(self, thoth_endpoint="https://api.thoth.pub", version="0.4.2"):
        """Returns new ThothClient object at the specified GraphQL endpoint

        thoth_endpoint: Must be the full URL (eg. 'http://localhost').
        """
        self.thoth_endpoint = thoth_endpoint
        self.auth_endpoint = "{}/account/login".format(thoth_endpoint)
        self.graphql_endpoint = "{}/graphql".format(thoth_endpoint)
        self.client = GraphQLClient(self.graphql_endpoint)
        self.version = version.replace('.', '_')

        # this is the only 'magic' part for queries
        # it wires up the methods named in 'endpoints' list of a versioned
        # subclass (e.g. thoth_0_4_2) to this class, thereby providing the
        # methods that can be called for any API version
        if issubclass(ThothClient, type(self)):
            endpoints = \
                importlib.import_module('thothlibrary.thoth-{0}.'
                                        'endpoints'.format(self.version))
            version_endpoints = \
                getattr(endpoints,
                        'ThothClient{0}'.format(self.version))\
                    (version=version,
                     thoth_endpoint=thoth_endpoint)

            [setattr(self,
                     x,
                     getattr(version_endpoints,
                             x)) for x in version_endpoints.endpoints]

    def login(self, email, password):
        """Obtain an authentication token"""
        auth = ThothAuthenticator(self.auth_endpoint, email, password)
        bearer = "Bearer {}".format(auth.get_token())
        self.client.inject_token(bearer)

    def mutation(self, mutation_name, data):
        """Instantiate a thoth mutation and execute"""
        mutation = ThothMutation(mutation_name, data)
        return mutation.run(self.client)

    def query(self, query_name, parameters, raw=False):
        """Instantiate a thoth query and execute"""
        query = ThothQuery(query_name, parameters, self.QUERIES, raw=raw)
        return query.run(self.client)

    def create_publisher(self, publisher):
        """Construct and trigger a mutation to add a new publisher object"""
        return self.mutation("createPublisher", publisher)

    def create_imprint(self, imprint):
        """Construct and trigger a mutation to add a new imprint object"""
        return self.mutation("createImprint", imprint)

    def create_work(self, work):
        """Construct and trigger a mutation to add a new work object"""
        return self.mutation("createWork", work)

    def create_publication(self, publication):
        """Construct and trigger a mutation to add a new publication object"""
        return self.mutation("createPublication", publication)

    def create_price(self, price):
        """Construct and trigger a mutation to add a new price object"""
        return self.mutation("createPrice", price)

    def create_language(self, language):
        """Construct and trigger a mutation to add a new language object"""
        return self.mutation("createLanguage", language)

    def create_subject(self, subject):
        """Construct and trigger a mutation to add a new subject object"""
        return self.mutation("createSubject", subject)

    def create_series(self, series):
        """Construct and trigger a mutation to add a new series object"""
        return self.mutation("createSeries", series)

    def create_issue(self, issue):
        """Construct and trigger a mutation to add a new issue object"""
        return self.mutation("createIssue", issue)

    def create_contributor(self, contributor):
        """Construct and trigger a mutation to add a new contributor object"""
        return self.mutation("createContributor", contributor)

    def create_contribution(self, contribution):
        """Construct and trigger a mutation to add a new contribution object"""
        return self.mutation("createContribution", contribution)

    def supported_versions(self):
        regex = 'thoth-(\d+_\d+_\d+)'

        versions = []

        for module in pkgutil.iter_modules(thothlibrary.__path__):
            match = re.match(regex, module.name)

            if match:
                versions.append(match.group(1).replace('_', '.'))

        return versions

    def _api_request(self, endpoint_name: str, parameters,
                     return_raw: bool = False):
        """
        Makes a request to the API
        @param endpoint_name: the name of the endpoint
        @param return_raw: whether to return the raw data or an object (default)
        @param parameters: the parameters to pass to GraphQL
        @return: an object or JSON of the request
        """
        response = self.query(endpoint_name, parameters, raw=return_raw)

        if return_raw:
            return response
        else:
            return self._build_structure(endpoint_name, response)

    def _build_structure(self, endpoint_name, data):
        """
        Builds an object structure for an endpoint
        @param endpoint_name: the name of the endpoint
        @param data: the data
        @return: an object form of the output
        """
        structures = \
            importlib.import_module(
                'thothlibrary.thoth-{0}.structures'.format(self.version))
        builder = structures.StructureBuilder(endpoint_name, data)
        return builder.create_structure()

    @staticmethod
    def _dictionary_append(input_dict, key, value):
        if value:
            input_dict[key] = value
        return input_dict

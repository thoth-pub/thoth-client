"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020 and (c) ΔQ Programming LLP, July 2021
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import importlib
import pkgutil

import re
import thothlibrary
from .auth import ThothAuthenticator
from .errors import ResponseEmptyError
from .graphql import GraphQLClientRequests as GraphQLClient
from .mutation import ThothMutation
from .query import ThothQuery

THOTH_ENDPOINT = "https://api.thoth.pub"
THOTH_VERSION = "0.9.0"


class ThothClient:
    """Client to Thoth's GraphQL API"""
    QUERIES = {}  # populated according to each version's requirements

    def __new__(cls, thoth_endpoint=THOTH_ENDPOINT, version=THOTH_VERSION):
        # this new call is the only bit of "magic"
        # it basically subs in the sub-class of the correct version and returns
        # an instance of that, instead of the generic class
        version_replaced = version.replace('.', '_')
        module = 'thothlibrary.thoth-{0}.endpoints'.format(version_replaced)
        endpoints = importlib.import_module(module)

        version_endpoints = getattr(
            endpoints, 'ThothClient{0}'.format(version_replaced))

        return version_endpoints(thoth_endpoint=thoth_endpoint,
                                 version=version)

    def __init__(self, thoth_endpoint=THOTH_ENDPOINT, version=THOTH_VERSION):
        """Returns new ThothClient object at the specified GraphQL endpoint

        thoth_endpoint: Must be the full URL (eg. 'http://localhost').
        """
        self.thoth_endpoint = thoth_endpoint
        self.auth_endpoint = "{}/account/login".format(thoth_endpoint)
        self.graphql_endpoint = "{}/graphql".format(thoth_endpoint)
        self.client = GraphQLClient(self.graphql_endpoint)
        self.version = version.replace('.', '_')

    def login(self, email, password):
        """Obtain an authentication token"""
        auth = ThothAuthenticator(self.auth_endpoint, email, password)
        bearer = "Bearer {}".format(auth.get_token())
        self.client.inject_token(bearer)

    def mutation(self, mutation_name, data, nested=True):
        """Instantiate a thoth mutation and execute it"""
        mutation = ThothMutation(mutation_name, data, nested)
        max_retries = 2
        for attempt in range(max_retries + 1):
            try:
                return mutation.run(self.client)
            except ResponseEmptyError:
                if attempt == max_retries:
                    raise

    def query(self, query_name, parameters, raw=False):
        """Instantiate a thoth query and execute"""
        query = ThothQuery(query_name, parameters, self.QUERIES, raw=raw)
        max_retries = 2
        for attempt in range(max_retries + 1):
            try:
                return query.run(self.client)
            except ResponseEmptyError:
                if attempt == max_retries:
                    raise

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

    def create_affiliation(self, affiliation):
        """Construct and trigger a mutation to add a new affiliation object"""
        return self.mutation("createAffiliation", affiliation)

    def create_institution(self, institution):
        """Construct and trigger a mutation to add a new institution object"""
        return self.mutation("createInstitution", institution)

    def create_location(self, location):
        """Construct and trigger a mutation to add a new location object"""
        return self.mutation("createLocation", location)

    def create_funding(self, funding):
        """Construct and trigger a mutation to add a new funding object"""
        return self.mutation("createFunding", funding)

    def create_work_relation(self, work_relation):
        """Construct and trigger a mutation to add a new work relation object"""
        return self.mutation("createWorkRelation", work_relation)

    def create_reference(self, reference):
        """Construct and trigger a mutation to add a new reference object"""
        return self.mutation("createReference", reference)

    def update_work(self, work):
        """Construct and trigger a mutation to update a work object"""
        return self.mutation("updateWork", work)

    def update_contributor(self, contributor):
        """Construct and trigger a mutation to update a contributor object"""
        return self.mutation("updateContributor", contributor)

    def update_institution(self, institution):
        """Construct and trigger a mutation to update an institution object"""
        return self.mutation("updateInstitution", institution)

    def update_location(self, location):
        """Construct and trigger a mutation to update a location object"""
        return self.mutation("updateLocation", location)
    
    def update_publication(self, publication):
        """Construct and trigger a mutation to update a publication object"""
        return self.mutation("updatePublication", publication)

    def update_price(self, price):
        """Construct and trigger a mutation to update a price object"""
        return self.mutation("updatePrice", price)

    def delete_location(self, location):
        """Construct and trigger a mutation to delete a location object"""
        return self.mutation("deleteLocation", location, nested=False)

    @staticmethod
    def supported_versions():
        """
        Shows the versions of Thoth that this API supports
        @return: a list of version strings
        """
        regex = r'thoth-(\d+_\d+_\d+)'

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
        @param return_raw: whether to return raw data or an object (default)
        @param parameters: the parameters to pass to GraphQL
        @return: an object or JSON of the request
        """
        response = self.query(endpoint_name, parameters, raw=return_raw)

        if return_raw:
            return response
        return self._build_structure(endpoint_name, response)

    def _build_structure(self, endpoint_name, data):
        """
        Builds an object structure for an endpoint
        @param endpoint_name: the name of the endpoint
        @param data: the data
        @return: an object form of the output
        """
        module = 'thothlibrary.thoth-{0}.structures'.format(self.version)
        structures = importlib.import_module(module)
        builder = getattr(structures, 'StructureBuilder')(endpoint_name, data)

        return builder.create_structure()

    @staticmethod
    def _dictionary_append(input_dict, key, value):
        """
        Either adds a value to a dictionary or doesn't if it's null
        @param input_dict: the dictionary to modify
        @param key: the key to add
        @param value: the value to add
        @return: the dictionary
        """
        if value:
            input_dict[key] = value
        return input_dict

"""
GraphQL client for Thoth

Copyright (c) 2026 Thoth Open Metadata
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import importlib

from munch import Munch

from .errors import ResponseEmptyError
from .graphql import GraphQLClientRequests as GraphQLClient
from .mutation import ThothMutation
from .query import ThothQuery

THOTH_ENDPOINT = "https://api.thoth.pub"
THOTH_VERSION = "1.0.0"
V1_MODULE = importlib.import_module("thothlibrary.thoth-1_0_0.endpoints")


class ThothClient:
    """Client to Thoth's GraphQL API."""
    QUERIES = V1_MODULE.QUERIES

    def __init__(self, thoth_endpoint=THOTH_ENDPOINT, version=THOTH_VERSION):
        """Returns a ThothClient object at the specified GraphQL endpoint."""
        if version != THOTH_VERSION:
            raise ValueError(
                "This client only supports Thoth schema version {0}".format(
                    THOTH_VERSION
                )
            )
        self.thoth_endpoint = thoth_endpoint
        self.graphql_endpoint = "{}/graphql".format(thoth_endpoint)
        self.client = GraphQLClient(self.graphql_endpoint)
        self.version = THOTH_VERSION

    def set_token(self, token):
        """Inject a personal access token for authenticated requests."""
        bearer = "Bearer {}".format(token)
        self.client.inject_token(bearer)

    def login(self, token):
        """Alias for PAT-based authentication."""
        self.set_token(token)

    def mutation(self, mutation_name, data, nested=True, extra_args=None):
        """Instantiate a thoth mutation and execute it"""
        mutation = ThothMutation(mutation_name, data, nested,
                                 extra_args=extra_args)
        max_retries = 2
        for attempt in range(max_retries + 1):
            try:
                result = mutation.run(self.client)
                if isinstance(result, dict):
                    return Munch.fromDict(result)
                if isinstance(result, list):
                    return [
                        Munch.fromDict(item) if isinstance(item, dict)
                        else item for item in result
                    ]
                return result
            except ResponseEmptyError:
                if attempt == max_retries:
                    raise

    def query(self, query_name, parameters, raw=False, fields=None):
        """Instantiate a thoth query and execute"""
        query = ThothQuery(
            query_name,
            parameters,
            self.QUERIES,
            raw=raw,
            fields=fields,
        )
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
        """Shows the only supported schema version."""
        return [THOTH_VERSION]

    def _api_request(self, endpoint_name: str, parameters,
                     return_raw: bool = False, fields=None):
        """
        Makes a request to the API
        @param endpoint_name: the name of the endpoint
        @param return_raw: whether to return raw data or an object (default)
        @param parameters: the parameters to pass to GraphQL
        @param fields: optional per-request GraphQL field selection override
        @return: an object or JSON of the request
        """
        response = self.query(
            endpoint_name,
            parameters,
            raw=return_raw,
            fields=fields,
        )

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
        structures = importlib.import_module("thothlibrary.thoth-1_0_0.structures")
        builder = getattr(structures, "StructureBuilder")(endpoint_name, data)

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


def _mutation_method(mutation_name, *, nested=True, markup=False):
    def _method(self, data, markup_format=None):
        extra_args = {}
        if markup and markup_format:
            extra_args["markupFormat"] = markup_format
        return self.mutation(mutation_name, data, nested=nested,
                             extra_args=extra_args or None)

    return _method


for method_name, mutation_name, nested, markup in [
    ("create_title", "createTitle", True, True),
    ("create_abstract", "createAbstract", True, True),
    ("create_biography", "createBiography", True, True),
    ("create_additional_resource", "createAdditionalResource", True, True),
    ("create_award", "createAward", True, True),
    ("create_endorsement", "createEndorsement", True, True),
    ("create_book_review", "createBookReview", True, True),
    ("create_work_featured_video", "createWorkFeaturedVideo", True, False),
    ("create_contact", "createContact", True, False),
    ("update_publisher", "updatePublisher", True, False),
    ("update_imprint", "updateImprint", True, False),
    ("update_contribution", "updateContribution", True, False),
    ("update_series", "updateSeries", True, False),
    ("update_issue", "updateIssue", True, False),
    ("update_language", "updateLanguage", True, False),
    ("update_funding", "updateFunding", True, False),
    ("update_subject", "updateSubject", True, False),
    ("update_affiliation", "updateAffiliation", True, False),
    ("update_work_relation", "updateWorkRelation", True, False),
    ("update_reference", "updateReference", True, False),
    ("update_additional_resource", "updateAdditionalResource", True, True),
    ("update_award", "updateAward", True, True),
    ("update_endorsement", "updateEndorsement", True, True),
    ("update_book_review", "updateBookReview", True, True),
    ("update_work_featured_video", "updateWorkFeaturedVideo", True, False),
    ("update_contact", "updateContact", True, False),
    ("update_title", "updateTitle", True, True),
    ("update_abstract", "updateAbstract", True, True),
    ("update_biography", "updateBiography", True, True),
    ("delete_work", "deleteWork", False, False),
    ("delete_publisher", "deletePublisher", False, False),
    ("delete_imprint", "deleteImprint", False, False),
    ("delete_contributor", "deleteContributor", False, False),
    ("delete_contribution", "deleteContribution", False, False),
    ("delete_publication", "deletePublication", False, False),
    ("delete_series", "deleteSeries", False, False),
    ("delete_issue", "deleteIssue", False, False),
    ("delete_language", "deleteLanguage", False, False),
    ("delete_title", "deleteTitle", False, False),
    ("delete_institution", "deleteInstitution", False, False),
    ("delete_funding", "deleteFunding", False, False),
    ("delete_price", "deletePrice", False, False),
    ("delete_subject", "deleteSubject", False, False),
    ("delete_affiliation", "deleteAffiliation", False, False),
    ("delete_work_relation", "deleteWorkRelation", False, False),
    ("delete_reference", "deleteReference", False, False),
    ("delete_additional_resource", "deleteAdditionalResource", False, False),
    ("delete_award", "deleteAward", False, False),
    ("delete_endorsement", "deleteEndorsement", False, False),
    ("delete_book_review", "deleteBookReview", False, False),
    ("delete_work_featured_video", "deleteWorkFeaturedVideo", False, False),
    ("delete_abstract", "deleteAbstract", False, False),
    ("delete_biography", "deleteBiography", False, False),
    ("delete_contact", "deleteContact", False, False),
    ("move_affiliation", "moveAffiliation", False, False),
    ("move_contribution", "moveContribution", False, False),
    ("move_issue", "moveIssue", False, False),
    ("move_reference", "moveReference", False, False),
    ("move_additional_resource", "moveAdditionalResource", False, False),
    ("move_award", "moveAward", False, False),
    ("move_endorsement", "moveEndorsement", False, False),
    ("move_book_review", "moveBookReview", False, False),
    ("move_subject", "moveSubject", False, False),
    ("move_work_relation", "moveWorkRelation", False, False),
    ("init_publication_file_upload", "initPublicationFileUpload", True, False),
    ("init_frontcover_file_upload", "initFrontcoverFileUpload", True, False),
    ("init_additional_resource_file_upload",
     "initAdditionalResourceFileUpload", True, False),
    ("init_work_featured_video_file_upload",
     "initWorkFeaturedVideoFileUpload", True, False),
    ("complete_file_upload", "completeFileUpload", True, False),
]:
    setattr(ThothClient, method_name,
            _mutation_method(mutation_name, nested=nested, markup=markup))


for method_name, (query_name, arg_name, gql_arg_name) in V1_MODULE.SINGLE_ID_QUERIES.items():
    setattr(
        ThothClient,
        method_name,
        V1_MODULE._single_id_method(
            query_name,
            arg_name,
            gql_arg_name,
            markup=method_name in {"title", "abstract", "biography"},
            work_markup=method_name in V1_MODULE.WORK_QUERY_METHODS,
        ),
    )

for method_name, (query_name, arg_name) in V1_MODULE.SINGLE_DOI_QUERIES.items():
    setattr(
        ThothClient,
        method_name,
        V1_MODULE._single_doi_method(
            query_name,
            arg_name,
            work_markup=method_name in V1_MODULE.WORK_QUERY_METHODS,
        ),
    )

for method_name, (query_name, mapping) in V1_MODULE.LIST_QUERIES.items():
    setattr(
        ThothClient,
        method_name,
        V1_MODULE._list_method(
            query_name,
            mapping,
            work_markup=method_name in V1_MODULE.WORK_QUERY_METHODS,
        ),
    )

for method_name, (query_name, mapping) in V1_MODULE.COUNT_QUERIES.items():
    setattr(ThothClient, method_name,
            V1_MODULE._count_method(query_name, mapping))

ThothClient._quote = staticmethod(V1_MODULE.ThothClient1_0_0._quote)

for helper_name in [
    "_query_parameters",
    "_single_id_request",
    "_single_doi_request",
]:
    setattr(ThothClient, helper_name,
            getattr(V1_MODULE.ThothClient1_0_0, helper_name))

ThothClient.bookIds = V1_MODULE.ThothClient1_0_0.bookIds

"""
GraphQL client for Thoth

(c) Open Book Publishers, February 2020
This programme is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""


from graphqlclient import GraphQLClient
from .auth import ThothAuthenticator
from .mutation import ThothMutation
from .query import ThothQuery


class ThothClient():
    """Client to Thoth's GraphQL API"""

    def __init__(self, thoth_endpoint="https://api.thoth.pub"):
        """Returns new ThothClient object at the specified GraphQL endpoint

        thoth_endpoint: Must be the full URL (eg. 'http://localhost').
        """
        self.auth_endpoint = "{}/account/login".format(thoth_endpoint)
        self.graphql_endpoint = "{}/graphql".format(thoth_endpoint)
        self.client = GraphQLClient(self.graphql_endpoint)

    def login(self, email, password):
        """Obtain an authentication token"""
        auth = ThothAuthenticator(self.auth_endpoint, email, password)
        bearer = "Bearer {}".format(auth.get_token())
        self.client.inject_token(bearer)

    def mutation(self, mutation_name, data):
        """Instantiate a thoth mutation and execute"""
        mutation = ThothMutation(mutation_name, data)
        return mutation.run(self.client)

    def query(self, query_name, parameters):
        """Instantiate a thoth query and execute"""
        query = ThothQuery(query_name, parameters)
        return query.run(self.client)

    def works(self, limit: int = 100, offset: int = 0, filter_str: str = ""):
        """Construct and trigger a query to obtain all works"""
        parameters = {
            "limit": limit,
            "offset": offset,
            "filter": filter_str,
        }
        return self.query("works", parameters)

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

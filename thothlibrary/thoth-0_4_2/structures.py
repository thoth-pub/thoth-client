"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import collections

from munch import Munch
from datetime import datetime


def _muncher_repr(obj):
    """
    This is a hacky munch context switcher. It passes the original __repr__
    pointer back
    @param obj: the object to represent
    @return: the original munch representation
    """
    Munch.__repr__ = munch_local
    return obj.__repr__()


def _parse_authors(obj):
    """
    This parses a list of contributors into authors and editors
    @param obj: the Work to parse
    @return: a string representation of authors
    """
    if not 'contributions' in obj:
        return None

    author_dict = {}
    authors = ''

    for contributor in obj.contributions:
        if contributor.contributionType == 'AUTHOR':
            author_dict[contributor.contributionOrdinal] = contributor.fullName
        if contributor.contributionType == "EDITOR":
            author_dict[contributor.contributionOrdinal] = \
                contributor.fullName + " (ed.)"

    od_authors = collections.OrderedDict(sorted(author_dict.items()))

    for k, v in od_authors.items():
        authors += contributor.fullName + ', '

    return authors


def __price_parser(prices):
    if len(prices) > 0 and 'currencyCode' not in prices:
        return '({0}{1})'.format(prices[0].unitPrice, prices[0].currencyCode)
    elif 'currencyCode' in prices:
        return '{0}{1}'.format(prices.unitPrice, prices.currencyCode)
    else:
        return ''


# these are lambda function formatting statements for the endpoints
# they are injected to replace the default dictionary (Munch) __repr__ and
# __str__ methods. They let us create nice-looking string representations
# of objects, such as books
default_fields = {'works': lambda
    self: f'{_parse_authors(self)}{self.fullTitle} ({self.place}: {self.imprint.publisher.publisherName}, {datetime.strptime(self.publicationDate, "%Y-%m-%d").year if self.publicationDate else "n.d."}) [{self.workId}]' if '__typename' in self and self.__typename == 'Work' else f'{_muncher_repr(self)}',
                  'prices': lambda
                      self: f'{self.publication.work.fullTitle} ({self.publication.work.place}: {self.publication.work.imprint.publisher.publisherName}, {datetime.strptime(self.publication.work.publicationDate, "%Y-%m-%d").year if self.publication.work.publicationDate else "n.d."}) '
                            f'costs {__price_parser(self)} [{self.priceId}]' if '__typename' in self and self.__typename == 'Price' else f'{_muncher_repr(self)}',
                  'price': lambda
                      self: f'{self.publication.work.fullTitle} ({self.publication.work.place}: {self.publication.work.imprint.publisher.publisherName}, {datetime.strptime(self.publication.work.publicationDate, "%Y-%m-%d").year if self.publication.work.publicationDate else "n.d."}) '
                            f'costs {__price_parser(self)} [{self.priceId}]' if '__typename' in self and self.__typename == 'Price' else f'{_muncher_repr(self)}',
                  'publications': lambda
                      self: f'{_parse_authors(self.work)}{self.work.fullTitle} ({self.work.place}: {self.work.imprint.publisher.publisherName}, {datetime.strptime(self.work.publicationDate, "%Y-%m-%d").year if self.work.publicationDate else "n.d."}) '
                            f'[{self.publicationType}] {__price_parser(self.prices)} [{self.publicationId}]' if '__typename' in self and self.__typename == 'Publication' else f'{_muncher_repr(self)}',
                  'workByDoi': lambda
                      self: f'{_parse_authors(self)}{self.fullTitle} ({self.place}: {self.imprint.publisher.publisherName}, {datetime.strptime(self.publicationDate, "%Y-%m-%d").year if self.publicationDate else "n.d."})' if '__typename' in self and self.__typename == 'Work' else f'{_muncher_repr(self)}',
                  'work': lambda
                      self: f'{_parse_authors(self)}{self.fullTitle} ({self.place}: {self.imprint.publisher.publisherName}, {datetime.strptime(self.publicationDate, "%Y-%m-%d").year if self.publicationDate else "n.d."})' if '__typename' in self and self.__typename == 'Work' else f'{_muncher_repr(self)}',
                  'publishers': lambda
                      self: f'{self.publisherName} ({self.publisherId})' if '__typename' in self and self.__typename == 'Publisher' else f'{_muncher_repr(self)}',
                  'imprints': lambda
                      self: f'{self.imprintName} ({self.publisher.publisherName}/{self.publisherId}) [{self.imprintId}]' if '__typename' in self and self.__typename == 'Imprint' else f'{_muncher_repr(self)}',
                  'imprint': lambda
                      self: f'{self.imprintName} ({self.publisher.publisherName}/{self.publisherId}) [{self.imprintId}]' if '__typename' in self and self.__typename == 'Imprint' else f'{_muncher_repr(self)}',
                  'contributions': lambda
                      self: f'{self.fullName} ({self.contributionType} of {self.work.fullTitle}) [{self.contributionId}]' if '__typename' in self and self.__typename == 'Contribution' else f'{_muncher_repr(self)}',
                  'contribution': lambda
                      self: f'{self.fullName} ({self.contributionType} of {self.work.fullTitle}) [{self.contributionId}]' if '__typename' in self and self.__typename == 'Contribution' else f'{_muncher_repr(self)}',
                  'contributors': lambda
                      self: f'{self.fullName} ({self.contributions[0].contributionType} of {self.contributions[0].work.fullTitle}) [{self.contributorId}]' if '__typename' in self and self.__typename == 'Contributor' else f'{_muncher_repr(self)}',
                  'contributor': lambda
                      self: f'{self.fullName} ({self.contributions[0].contributionType} of {self.contributions[0].work.fullTitle}) [{self.contributorId}]' if '__typename' in self and self.__typename == 'Contributor' else f'{_muncher_repr(self)}',
                  'publication': lambda
                      self: f'{_parse_authors(self.work)}{self.work.fullTitle} ({self.work.place}: {self.work.imprint.publisher.publisherName}, {datetime.strptime(self.work.publicationDate, "%Y-%m-%d").year if self.work.publicationDate else "n.d."}) '
                            f'[{self.publicationType}] {__price_parser(self.prices)} [{self.publicationId}]' if '__typename' in self and self.__typename == 'Publication' else f'{_muncher_repr(self)}',
                  'serieses': lambda
                      self: f'{self.seriesName} ({self.imprint.publisher.publisherName}) [{self.seriesId}]' if '__typename' in self and self.__typename == 'Series' else f'{_muncher_repr(self)}',
                  'series': lambda
                      self: f'{self.seriesName} ({self.imprint.publisher.publisherName}) [{self.seriesId}]' if '__typename' in self and self.__typename == 'Series' else f'{_muncher_repr(self)}',
                  'issues': lambda
                      self: f'{self.work.fullTitle} in {self.series.seriesName} ({self.series.imprint.publisher.publisherName}) [{self.issueId}]' if '__typename' in self and self.__typename == 'Issue' else f'{_muncher_repr(self)}',
                  'issue': lambda
                      self: f'{self.work.fullTitle} in {self.series.seriesName} ({self.series.imprint.publisher.publisherName}) [{self.issueId}]' if '__typename' in self and self.__typename == 'Issue' else f'{_muncher_repr(self)}',
                  'subjects': lambda
                      self: f'{self.work.fullTitle} is in the {self.subjectCode} subject area ({self.subjectType}) [{self.subjectId}]' if '__typename' in self and self.__typename == 'Subject' else f'{_muncher_repr(self)}',
                  'subject': lambda
                      self: f'{self.work.fullTitle} is in the {self.subjectCode} subject area ({self.subjectType}) [{self.subjectId}]' if '__typename' in self and self.__typename == 'Subject' else f'{_muncher_repr(self)}',
                  'funders': lambda
                      self: f'{self.funderName} funded {len(self.fundings)} books [{self.funderId}]' if '__typename' in self and self.__typename == 'Funder' else f'{_muncher_repr(self)}',
                  'languages': lambda
                      self: f'{self.work.fullTitle} is in {self.languageCode} ({self.languageRelation}) [{self.languageId}]' if '__typename' in self and self.__typename == 'Language' else f'{_muncher_repr(self)}',
                  'language': lambda
                      self: f'{self.work.fullTitle} is in {self.languageCode} ({self.languageRelation}) [{self.languageId}]' if '__typename' in self and self.__typename == 'Language' else f'{_muncher_repr(self)}',
                  'publisher': lambda
                      self: f'{self.publisherName} ({self.publisherId})' if '__typename' in self and self.__typename == 'Publisher' else f'{_muncher_repr(self)}'}

# this stores the original function pointer of Munch.__repr__ so that we can
# re-inject it above in "_muncher_repr"
munch_local = Munch.__repr__


class StructureBuilder:
    """A class to build a Thoth object structure"""

    def __init__(self, structure, data):
        self.structure = structure
        self.data = data

    def create_structure(self):
        """
        Creates an object structure from dictionary input
        @return: an object
        """
        structures = []
        if isinstance(self.data, list):
            for item in self.data:
                x = self._munch(item)
                structures.append(x)
        else:
            x = self._munch(self.data)
            return x

        return structures

    def _munch(self, item):
        """
        Converts our JSON or dict object into an addressable object.
        Also sets up the Munch __repr__ and __str__ functions.
        @param item: the item to convert
        @return: a converted object with string representation
        """
        x = Munch.fromDict(item)
        if self.structure in default_fields.keys():
            struct = default_fields[self.structure]
            Munch.__repr__ = Munch.__str__
            Munch.__str__ = struct
        return x

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
            author_dict[contributor.contributionOrdinal] = contributor.fullName + " (ed.)"

    od_authors = collections.OrderedDict(sorted(author_dict.items()))

    for k, v in od_authors.items():
        authors += contributor.fullName + ', '

    return authors


def __price_parser(prices):
    if len(prices) > 0:
        return '({0}{1})'.format(prices[0].unitPrice, prices[0].currencyCode)
    else:
        return ''


# these are lambda function formatting statements for the endpoints
# they are injected to replace the default dictionary (Munch) __repr__ and
# __str__ methods. They let us create nice-looking string representations
# of objects, such as books
default_fields = {'works': lambda self: f'{_parse_authors(self)}{self.fullTitle} ({self.place}: {self.imprint.publisher.publisherName}, {datetime.strptime(self.publicationDate, "%Y-%m-%d").year if self.publicationDate else "n.d."})' if self.__typename == 'Work' else f'{_muncher_repr(self)}',
                  'publications': lambda self: f'{_parse_authors(self.work)}{self.work.fullTitle} ({self.work.place}: {self.work.imprint.publisher.publisherName}, {datetime.strptime(self.work.publicationDate, "%Y-%m-%d").year if self.work.publicationDate else "n.d."}) '
                                               f'[{self.publicationType}] {__price_parser(self.prices)} [{self.publicationId}]' if self.__typename == 'Publication' else f'{_muncher_repr(self)}',
                  'workByDoi': lambda self: f'{_parse_authors(self)}{self.fullTitle} ({self.place}: {self.imprint.publisher.publisherName}, {datetime.strptime(self.publicationDate, "%Y-%m-%d").year if self.publicationDate else "n.d."})' if self.__typename == 'Work' else f'{_muncher_repr(self)}',
                  'publishers': lambda self: f'{self.publisherName} ({self.publisherId})' if self.__typename == 'Publisher' else f'{_muncher_repr(self)}',
                  'contributions': lambda self: f'{self.fullName} ({self.contributionType}) [{self.contributionId}]' if self.__typename == 'Contribution' else f'{_muncher_repr(self)}',
                  'publisher': lambda self: f'{self.publisherName} ({self.publisherId})' if self.__typename == 'Publisher' else f'{_muncher_repr(self)}'}

# this stores the original function pointer of Munch.__repr__ so that we can
# reinect it above in "muncher"
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

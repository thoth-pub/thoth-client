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


default_fields = {'works': lambda self: f'{_parse_authors(self)}{self.fullTitle} ({self.place}: {self.imprint.publisher.publisherName}, {datetime.strptime(self.publicationDate, "%Y-%m-%d").year if self.publicationDate else "n.d."})' if self.__typename == 'Work' else f'{muncher(self)}',
                  'publishers': lambda self: f'{self.publisherName} ({self.publisherId})' if self.__typename == 'Publisher' else f'{muncher(self)}'}

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

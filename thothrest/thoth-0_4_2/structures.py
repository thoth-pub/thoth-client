"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from munch import Munch

default_fields = {'formats': 'id',
                  'format': 'name',
                  'specifications': 'name',
                  'specification': 'name',
                  'platforms': 'name',
                  'platform': 'name'}


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
        Converts our JSON or dict object into an addressable object
        @param item: the item to convert
        @return: a converted object with string representation
        """
        x = Munch.fromDict(item)
        if self.structure in default_fields.keys():
            struct = default_fields[self.structure]
            Munch.__repr__ = Munch.__str__
            Munch.__str__ = lambda self: self[struct]
        return x

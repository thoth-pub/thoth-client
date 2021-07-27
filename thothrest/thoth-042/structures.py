"""
(c) ΔQ Programming LLP, July 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from munch import Munch

default_fields = {'formats': 'id'}


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
        for item in self.data:
            x = Munch.fromDict(item)
            if self.structure in default_fields.keys():
                struct = default_fields[self.structure]
                Munch.__repr__ = Munch.__str__
                Munch.__str__ = lambda self: self[struct]
            structures.append(x)

        return structures

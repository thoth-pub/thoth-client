"""
Helpers to build object structures for the Thoth export API.

Copyright (c) 2026 Thoth Open Metadata
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
from munch import Munch


DEFAULT_FIELDS = {
    "formats": "id",
    "format": "name",
    "specifications": "name",
    "specification": "name",
    "platforms": "name",
    "platform": "name",
}


class StructureBuilder:
    """Build object structures for export API responses."""

    def __init__(self, structure, data):
        self.structure = structure
        self.data = data

    def create_structure(self):
        """Convert dict/list responses into Munch objects."""
        if isinstance(self.data, list):
            return [self._munch(item) for item in self.data]
        return self._munch(self.data)

    def _munch(self, item):
        x = Munch.fromDict(item)
        if self.structure in DEFAULT_FIELDS:
            struct = DEFAULT_FIELDS[self.structure]
            Munch.__repr__ = Munch.__str__
            Munch.__str__ = lambda self: self[struct]
        return x

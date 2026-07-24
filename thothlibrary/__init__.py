#!/usr/bin/env python3
"""GraphQL client for Thoth"""

__version__ = "1.2.0"
__author__ = "Javier Arias <javi@openbookpublishers.com>"
__copyright__ = "Copyright (c) 2026 Thoth Open Metadata"
__license__ = "Apache 2.0"

from .client import ThothClient
from .errors import ThothError
from .mutation import ThothMutation
from .query import ThothQuery
from .rest import ThothRESTClient

__all__ = [
    "ThothClient",
    "ThothQuery",
    "ThothMutation",
    "ThothRESTClient",
    "ThothError",
]

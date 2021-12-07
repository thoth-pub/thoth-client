"""
(c) ΔQ Programming LLP, 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import os
import pathlib

import requests
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    A management command that fetches and installs the latest ROR support
    """

    help = "Installs ROR functionality into Thoth components"

    def handle(self, *args, **options):
        url = 'https://zenodo.org/api/records/' \
              '?communities=ror-data&sort=mostrecent'

        meta_response = requests.get(url)

        print(meta_response)

        print("ROR fixtures installed. At next Thoth sync, ROR functionality "
              "will be enabled.")

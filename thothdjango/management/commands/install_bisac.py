"""
(c) ΔQ Programming LLP, 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import os
import pathlib

from django.core.management.base import BaseCommand
import csv

from thoth.models import BISAC


class Command(BaseCommand):
    """
    A management command that installs Bisac code support
    """

    help = "Installs Bisac code functionality into Thoth components"

    def handle(self, *args, **options):
        script_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        path = os.path.join(script_dir, 'fixtures', 'bisac.csv')

        if not os.path.isfile(path):
            print('Please place bisac.csv, converted from the BISAC mapping at '
                  'https://www.editeur.org/151/Thema/, '
                  'in the thoth/fixtures directory.')
            return

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                bisac_model = BISAC.objects.get_or_create(
                    code=row['BISAC Code'],
                    heading=row['Thema Literal 1'])[0]

                bisac_model.save()

        print("BISAC fixtures installed. At next Thoth sync, subject codes "
              "will be linked to BISAC entries.")

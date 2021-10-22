"""
(c) ΔQ Programming LLP, 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import os
import pathlib

from django.core.management.base import BaseCommand
import csv

from thoth.models import BIC


class Command(BaseCommand):
    """
    A management command that installs BIC code support
    """

    help = "Installs BIC code functionality into Thoth components"

    def handle(self, *args, **options):
        script_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        path = os.path.join(script_dir, 'fixtures', 'BIC.csv')
        path_quals = os.path.join(script_dir, 'fixtures', 'BICQuals.csv')

        if not os.path.isfile(path) or not os.path.isfile(path_quals):
            print('Please place BIC.csv and BICQuals.csv, converted from '
                  'https://www.bic.org.uk/7/BIC-Standard-Subject-Categories/, '
                  'in the thoth/fixtures directory.')
            return

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bic_model = BIC.objects.get_or_create(
                    code=row['Code'],
                    heading=row['Heading'])[0]

                bic_model.save()

        with open(path_quals, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                bic_model = BIC.objects.get_or_create(
                    code=row['Code'],
                    heading=row['Heading'])[0]

                bic_model.save()

        print("BIC fixtures installed. At next Thoth sync, subject codes will "
              "be linked to BIC entries.")

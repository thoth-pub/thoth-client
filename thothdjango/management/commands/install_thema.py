"""
(c) ΔQ Programming LLP, 2021
This program is free software; you may redistribute and/or modify
it under the terms of the Apache License v2.0.
"""
import os
import pathlib

from django.core.management.base import BaseCommand
import csv

from thoth.models import Thema


class Command(BaseCommand):
    """
    A management command that installs Thema code support
    """

    help = "Installs Thema code functionality into Thoth components"

    def handle(self, *args, **options):
        script_dir = pathlib.Path(__file__).parent.parent.parent.resolve()
        path = os.path.join(script_dir, 'fixtures', 'thema.csv')

        if not os.path.isfile(path):
            print('Please place thema.csv, converted from '
                  'https://www.editeur.org/151/Thema/, '
                  'in the thoth/fixtures directory.')
            return

        with open(path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                thema_model = Thema.objects.get_or_create(
                    code=row['Code'],
                    heading=row['English Heading'])[0]

                thema_model.save()

        print("Thema fixtures installed. At next Thoth sync, subject codes "
              "will be linked to THEMA entries.")

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import os
import sys
import django

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MarvelAPI.settings')
django.setup()

from application.models import Hero, Villain, EntityStat


class DataLoader():

    def __init__(self, parsed_args):

        self.filepath = parsed_args["filepath"]
        self.model_name = parsed_args["model"]
        self.model = globals()[self.model_name]

    def execute(self):

        with open(self.filepath) as csv_file:
            csv_entries = list(csv.DictReader(csv_file))

            errors = []
            successes = []

            for index, entry in enumerate(csv_entries, start=2):
                print(
                    "Importing row {0}/{1}..."
                    .format(index, len(csv_entries) + 1)
                )

                # Map CSV row values to model fields
                # If value not provided for given key, set to None
                attributes = {}
                for key, value in entry.items():
                    attributes[
                        key.strip().replace(' ', '_').lower()
                    ] = value if value else None

                # ID field must be provided for Hero and Villain imports
                if self.model in [Hero, Villain] and not attributes['id']:
                    errors.append(
                        'Row {0}: "id" column must be populated"'
                        .format(csv_entries.index(entry))
                    )
                    continue

                # Attempt to get matching record, else create record
                try:
                    # Duplicate check Hero/Villain imports on "id"
                    if self.model in [Hero, Villain]:
                        record, was_created = self.model.objects.get_or_create(
                            id=attributes['id'],
                            defaults=attributes
                        )
                    # Duplicate check EntityStat import across all fields
                    else:
                        record, was_created = self.model.objects.get_or_create(
                            **attributes
                        )

                # Error occured when attempting to get or create
                except Exception as exception:
                    errors.append(
                        "Row {0}: Exception raised {1}"
                        .format(index, exception)
                    )
                    continue

                # Record was created
                if was_created:
                    successes.append(
                        "Row {0}: Created {1}".format(index, record)
                    )

                # Record already existed in database
                else:
                    errors.append(
                        "Row {0}: Record already exists".format(index)
                    )

        # Display import summary
        print(
            "\nSuccessful imports: {success_count}"
            "\nFailed imports: {error_count}"
            .format(
                success_count=len(successes),
                error_count=len(errors)
            )
        )

        # Display import errors
        for error in errors:
            print("\t" + error)

        return successes, errors


def get_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        description='Load CSV data into Django Models'
    )

    parser.add_argument(
        '-f',
        '--filepath',
        dest='filepath',
        type=str,
        help='.csv to parse and load',
        required=True
    )

    parser.add_argument(
        '-m',
        '--model',
        dest='model',
        type=str,
        choices=['Hero', 'Villain', 'EntityStat'],
        help='Django model to write .csv data to',
        required=True
    )

    return vars(parser.parse_args())


if __name__ == '__main__':
    DataLoader(
        get_arguments()
    ).execute()

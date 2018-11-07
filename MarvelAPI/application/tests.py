# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import tempfile

from json import loads, dumps

from django.test import TestCase
from django.urls import reverse
from application.models import EntityStat, Hero, Villain
from application.import_csv import DataLoader
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase

HERO_VARS = {
    'id': 123,
    'align': 'align',
    'sex': 'sex',
    'eye': 'eye',
    'first_appearance': 'first_appearance',
    'identity': 'identity',
    'name': 'name',
    'alive': 'alive',
    'year': 2018,
    'hair': 'hair'
}
HERO_STAT_VARS = {
    'entity_id': HERO_VARS['id'],
    'metric_id': 'metric_id',
    'year': 2018,
    'value': 999
}
VILLAIN_VARS = {
    'id': 456,
    'align': 'align',
    'sex': 'sex',
    'eye': 'eye',
    'first_appearance': 'first_appearance',
    'identity': 'identity',
    'name': 'name',
    'alive': 'alive',
    'year': 2005,
    'hair': 'hair',
    'at_large': 'at_large'
}
VILLAIN_STAT_VARS = {
    'entity_id': VILLAIN_VARS['id'],
    'metric_id': 'metric_id',
    'year': 2005,
    'value': 333
}


class CSVImportTestSuite(TestCase):
    def setUp(self):
        self.csv_file = tempfile.NamedTemporaryFile(mode='w', delete=True)

    def setup_temp_csv(self, args):
        writer = csv.DictWriter(
            self.csv_file,
            fieldnames=args.keys()
        )
        writer.writeheader()
        writer.writerow(args)
        self.csv_file.seek(0)

    def test_hero_import(self):

        self.setup_temp_csv(HERO_VARS)

        successes, errors = DataLoader({
            "filepath": self.csv_file.name,
            "model": "Hero"
        }).execute()

        self.assertTrue(not errors)
        self.assertTrue(len(successes) == 1)
        self.assertTrue(Hero.objects.filter(**HERO_VARS).count() == 1)

        # Close and delete tempfile
        self.csv_file.close()

    def test_villan_import(self):
        self.setup_temp_csv(VILLAIN_VARS)

        successes, errors = DataLoader({
            "filepath": self.csv_file.name,
            "model": "Villain"
        }).execute()

        self.assertTrue(not errors)
        self.assertTrue(len(successes) == 1)
        self.assertTrue(Villain.objects.filter(**VILLAIN_VARS).count() == 1)

        # Close and delete tempfile
        self.csv_file.close()

    def test_stats_csv_extract(self):
        self.setup_temp_csv(HERO_STAT_VARS)

        # EntityStat import will validate that the
        # appropriate Entity model object exists first
        Hero.objects.create(**HERO_VARS)

        successes, errors = DataLoader({
            "filepath": self.csv_file.name,
            "model": "EntityStat"
        }).execute()

        self.assertTrue(not errors)
        self.assertTrue(len(successes) == 1)
        self.assertTrue(
            EntityStat.objects.filter(**HERO_STAT_VARS).count() == 1
        )

        # Close and delete tempfile
        self.csv_file.close()


class APITestSuite(APITestCase, URLPatternsTestCase):

    # Import API URLs
    from MarvelAPI.urls import urlpatterns

    def setUp(self):
        self.hero_obj = Hero.objects.create(**HERO_VARS)
        self.hero_stat_obj = EntityStat.objects.create(**HERO_STAT_VARS)

        self.villain_obj = Villain.objects.create(**VILLAIN_VARS)
        self.villain_stat_obj = \
            EntityStat.objects.create(**VILLAIN_STAT_VARS)

    def test_get_hero_list(self):

        url = reverse('hero_list')

        # Get response and convert OrderedDict return to dict
        response = self.client.get(url, format='json')
        data = loads(dumps(response.data))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], HERO_VARS)

    def test_select_hero(self):

        url = reverse('hero_select', kwargs={'id': self.hero_obj.id})

        # Get API response
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, HERO_VARS)

    def test_get_hero_stat(self):

        url = reverse('hero_stats', kwargs={'id': self.hero_obj.id})

        # Get response and convert OrderedDict return to dict
        response = self.client.get(url, format='json')
        data = loads(dumps(response.data))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], HERO_STAT_VARS)

    def test_get_villain_list(self):

        url = reverse('villain_list')

        # Get response and convert OrderedDict return to dict
        response = self.client.get(url, format='json')
        data = loads(dumps(response.data))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], VILLAIN_VARS)

    def test_select_villain(self):

        url = reverse('villain_select', kwargs={'id': self.villain_obj.id})

        # Get API response
        response = self.client.get(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, VILLAIN_VARS)

    def test_get_villain_stat(self):

        url = reverse('villain_stats', kwargs={'id': self.villain_obj.id})

        # Get response and convert OrderedDict return to dict
        response = self.client.get(url, format='json')
        data = loads(dumps(response.data))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0], VILLAIN_STAT_VARS)

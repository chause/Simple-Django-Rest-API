# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Entity(models.Model):

    id = models.IntegerField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=100, null=False, blank=False)
    identity = models.CharField(max_length=100, null=True)
    align = models.CharField(max_length=100, null=True)
    eye = models.CharField(max_length=100, null=True)
    hair = models.CharField(max_length=100, null=True)
    sex = models.CharField(max_length=100, null=True)
    alive = models.CharField(max_length=100, null=True)
    first_appearance = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)

    class Meta:
        abstract = True
        app_label = 'application'


class Hero(Entity):

    def __str__(self):
        return "Hero {0} - {1}".format(self.id, self.name)


class Villain(Entity):

    at_large = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "Villain {0} - {1}".format(self.id, self.name)


class EntityStat(models.Model):

    entity_id = models.IntegerField(null=False)
    metric_id = models.CharField(max_length=100, null=False, blank=False)
    year = models.IntegerField(null=True)
    value = models.IntegerField(null=True)

    def __str__(self):
        return "EntityStat {0} - {1}".format(self.entity_id, self.metric_id)

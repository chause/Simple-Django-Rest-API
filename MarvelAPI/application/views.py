# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import response, views
from application.models import Hero, Villain, EntityStat
from application.serializers import \
    HeroSerializer, VillainSerializer, EntityStatSerializer


class HeroList(views.APIView):

    def get(self, request):
        record = Hero.objects.all()
        serializer = HeroSerializer(record, many=True)
        return response.Response(serializer.data)


class HeroSelect(views.APIView):

    def get(self, request, id):
        record = Hero.objects.get(id=id)
        serializer = HeroSerializer(record)
        return response.Response(serializer.data)


class HeroStats(views.APIView):

    def get(self, request, id):
        Hero.objects.get(id=id)
        records = EntityStat.objects.filter(entity_id=id)
        serializer = EntityStatSerializer(records, many=True)
        return response.Response(serializer.data)


class VillainList(views.APIView):

    def get(self, request):
        record = Villain.objects.all()
        serializer = VillainSerializer(record, many=True)
        return response.Response(serializer.data)


class VillainSelect(views.APIView):

    def get(self, request, id):
        record = Villain.objects.get(id=id)
        serializer = VillainSerializer(record)
        return response.Response(serializer.data)


class VillainStats(views.APIView):

    def get(self, request, id):
        Villain.objects.get(id=id)
        records = EntityStat.objects.filter(entity_id=id)
        serializer = EntityStatSerializer(records, many=True)
        return response.Response(serializer.data)

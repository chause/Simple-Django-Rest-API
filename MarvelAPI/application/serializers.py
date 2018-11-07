from rest_framework import serializers
from application.models import Hero, Villain, EntityStat


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class VillainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villain
        fields = '__all__'


class EntityStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntityStat
        fields = ('entity_id', 'metric_id', 'year', 'value')

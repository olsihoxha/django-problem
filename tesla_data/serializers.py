from rest_framework import serializers
from .models import CountryName1, TeslaModel1


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryName1
        fields = ['name']


class TeslaModelSerializer(serializers.ModelSerializer):
    origin = CountryNameSerializer()

    class Meta:
        model = TeslaModel1
        fields = ['model_name', 'price', 'origin']

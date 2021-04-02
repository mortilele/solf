from rest_framework import serializers

from solf.apps.common import models


class CityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'

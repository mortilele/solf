from rest_framework import serializers

from solf.apps.business import models


class FitnessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fitness
        fields = '__all__'

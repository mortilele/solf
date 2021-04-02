from rest_framework import serializers

from solf.apps.classes import models


class ClassListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Class
        fields = '__all__'

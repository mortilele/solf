from rest_framework import serializers

from solf.apps.classes import models


class ClassLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassLog
        fields = '__all__'

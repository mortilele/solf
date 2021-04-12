from rest_framework import serializers

from solf.apps.classes import models


class ClassUserEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassUserEntry
        fields = '__all__'

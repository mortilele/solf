from rest_framework import serializers

from solf.apps.classes import models


class ClassScheduleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassSchedule
        fields = '__all__'

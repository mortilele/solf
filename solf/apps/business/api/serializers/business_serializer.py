from rest_framework import serializers

from solf.apps.business import models


class BusinessListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Business
        fields = '__all__'

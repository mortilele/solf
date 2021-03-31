from rest_framework import serializers

from solf.apps.core import models


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'

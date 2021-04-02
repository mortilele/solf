from rest_framework import serializers

from solf.apps.core import models


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

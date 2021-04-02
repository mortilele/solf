from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.core.api.serializers import CategoryListSerializer
from solf.apps.core.models import Category


@extend_schema(tags=["category"])
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

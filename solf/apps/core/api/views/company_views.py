from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.core.api.serializers import CompanyListSerializer
from solf.apps.core.models import Company


@extend_schema(tags=["business"])
class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CompanyListSerializer
    queryset = Company.objects.all()

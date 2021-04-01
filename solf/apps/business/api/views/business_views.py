from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.business.api.serializers import BusinessListSerializer
from solf.apps.business.models import Business


@extend_schema(tags=["business"])
class BusinessViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BusinessListSerializer
    queryset = Business.objects.all()

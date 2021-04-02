from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.common.api.serializers import CityListSerializer
from solf.apps.common.models import City


@extend_schema(tags=["common"])
class CityViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CityListSerializer
    queryset = City.objects.all()

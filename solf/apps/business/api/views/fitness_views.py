from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.business.api.serializers import FitnessListSerializer
from solf.apps.business.models import Fitness


@extend_schema(tags=["business"])
class FitnessViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FitnessListSerializer
    queryset = Fitness.objects.all()

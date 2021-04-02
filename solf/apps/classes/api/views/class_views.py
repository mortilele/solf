from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.classes.api.serializers import ClassListSerializer
from solf.apps.classes.models import Class


@extend_schema(tags=["class"])
class ClassViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassListSerializer
    queryset = Class.objects.all()

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.classes.api.serializers import ClassLogListSerializer
from solf.apps.classes.models import ClassLog


@extend_schema(tags=["class"])
class ClassLogViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassLogListSerializer
    queryset = ClassLog.objects.all()

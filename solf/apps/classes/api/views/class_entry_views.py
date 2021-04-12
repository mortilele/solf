from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.classes.api.serializers import ClassUserEntrySerializer
from solf.apps.classes.models import ClassUserEntry


@extend_schema(tags=["class"])
class ClassEntryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassUserEntrySerializer
    queryset = ClassUserEntry.objects.all()

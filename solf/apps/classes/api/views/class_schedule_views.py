from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from solf.apps.classes.api.serializers import ClassScheduleListSerializer
from solf.apps.classes.models import ClassSchedule


@extend_schema(tags=["class"])
class ClassScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassScheduleListSerializer
    queryset = ClassSchedule.objects.all()

from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from solf.apps.classes import services
from solf.apps.classes.api.filters.class_schedule_filter import ClassScheduleFilter
from solf.apps.classes.api.serializers import ClassScheduleListSerializer, ClassUserEntrySerializer
from solf.apps.classes.models import ClassSchedule


@extend_schema(tags=["class"])
class ClassScheduleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassScheduleListSerializer
    queryset = ClassSchedule.objects.all()
    filter_class = ClassScheduleFilter

    def get_permissions(self):
        if self.action == 'sign_up':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

    @extend_schema(request=None, responses={200: ClassUserEntrySerializer})
    @action(detail=True, methods=["post"])
    def sign_up(self, request, *args, **kwargs):
        class_schedule = self.get_object()
        user_entry = services.sign_up_to_class(class_schedule, self.request.user)
        return Response(
            ClassUserEntrySerializer(user_entry).data
        )

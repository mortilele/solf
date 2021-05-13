from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from solf.apps.classes.api.serializers import ClassUserEntrySerializer
from solf.apps.classes.models import ClassUserEntry


@extend_schema(tags=["class"])
class ClassEntryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ClassUserEntrySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ClassUserEntry.objects.filter(
            user_pass_id__in=self.request.user.passes.all().values_list('id', flat=True)
        )

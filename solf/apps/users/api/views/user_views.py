from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from .. import serializers
from solf.apps.users.models import User


@extend_schema(tags=["users"])
class UserViewSet(
    mixins.CreateModelMixin, viewsets.GenericViewSet
):
    serializer_class = serializers.UserCreateSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return self.queryset.filter(id=self.request.user.id)

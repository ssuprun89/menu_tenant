from django_filters import rest_framework
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import ModelViewSet

from menu_tenant.permissions import RegisterAllowPermission
from users.models import User
from users.serializers import (
    BaseUserSerializer,
    UserCreateSerializer,
)


@extend_schema_view(
    list=extend_schema(tags=["user"], operation_id="List User"),
    retrieve=extend_schema(tags=["user"], operation_id="Detail User"),
    create=extend_schema(tags=["user"], operation_id="Create User"),
    update=extend_schema(tags=["user"], operation_id="Update User"),
    partial_update=extend_schema(tags=["user"], operation_id="Partial update User"),
    destroy=extend_schema(tags=["user"], operation_id="Delete User"),
)
class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = BaseUserSerializer
    permission_classes = (RegisterAllowPermission,)
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ("email",)

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return self.serializer_class

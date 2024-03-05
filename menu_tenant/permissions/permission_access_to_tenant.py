from rest_framework.permissions import BasePermission

from users.models import UserClient


class AccessToTenant(BasePermission):
    def has_permission(self, request, view):
        if request.user.service_user:
            return True
        return UserClient.objects.filter(user=request.user, client=request.tenant).exists()

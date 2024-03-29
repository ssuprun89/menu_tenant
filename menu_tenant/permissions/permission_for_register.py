from rest_framework.permissions import IsAuthenticated


class RegisterAllowPermission(IsAuthenticated):
    def has_permission(self, request, view):
        if request.method == "POST":
            return True
        else:
            return super().has_permission(request, view)

from django.utils import timezone


class TenantTimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tenant = request.tenant  # Access the current tenant object from the request
        if tenant and hasattr(tenant, "timezone"):
            timezone.activate(tenant.timezone)  # Set the timezone for the request
        else:
            timezone.deactivate()  # Reset to the default timezone if no tenant or timezone specified
        return self.get_response(request)

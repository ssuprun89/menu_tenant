from django.core.exceptions import DisallowedHost
from django.db import connection
from django.http import JsonResponse, HttpResponseNotFound
from django_tenants.middleware import TenantMainMiddleware
from django_tenants.utils import get_tenant_domain_model, get_tenant_model


class TenantMiddlewareCustom(TenantMainMiddleware):
    def get_tenant(self, domain_model, hostname, request):
        tenant = None
        if code := request.headers.get("Tenant-Code"):
            tenant = get_tenant_model().objects.filter(code=code).first()
        if not tenant:
            tenant = domain_model.objects.select_related("tenant").get(domain=hostname).tenant
        return tenant

    def process_request(self, request):
        # Connection needs first to be at the public schema, as this is where
        # the tenant metadata is stored.

        connection.set_schema_to_public()
        try:
            hostname = self.hostname_from_request(request)
        except DisallowedHost:
            return HttpResponseNotFound()

        domain_model = get_tenant_domain_model()
        try:
            tenant = self.get_tenant(domain_model, hostname, request)
        except domain_model.DoesNotExist:
            data = {
                "errors": [
                    f"No tenant for hostname {request.get_host()}",
                ],
                "data": {},
                "status": "failed",
            }
            return JsonResponse(data, status=404)

        tenant.domain_url = tenant.domains.filter(is_primary=True).first().domain
        request.tenant = tenant
        connection.set_tenant(request.tenant)
        self.setup_url_routing(request)

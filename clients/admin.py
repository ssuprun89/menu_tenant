from django.contrib import admin
from django.contrib.admin import StackedInline

from clients.models import Client, ClientBrand, ClientsHours, ClientContact, Domain
from users.models import UserClient


class DomainAdmin(StackedInline):
    model = Domain
    max_num = 1


class ClientBrandAdmin(StackedInline):
    model = ClientBrand
    max_num = 1


class ClientsHoursAdmin(StackedInline):
    model = ClientsHours
    max_num = 7


class ClientContactAdmin(StackedInline):
    model = ClientContact
    max_num = 1


class ClientModelAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "created_on", "domain")
    inlines = [DomainAdmin, ClientBrandAdmin, ClientsHoursAdmin, ClientContactAdmin]
    list_per_page = 100

    def owner(self, obj):
        if user_client := obj.user.filter(role=UserClient.UserRole.OWNER).first():
            return user_client.user.email

    def domain(self, obj):
        if domain_obj := obj.domains.filter(is_primary=True).first():
            return domain_obj.domain


admin.site.register(Client, ClientModelAdmin)
admin.site.register(Domain, admin.ModelAdmin)

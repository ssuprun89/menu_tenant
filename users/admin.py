from django.contrib import admin

from users.models import User


class ClientModelAdmin(admin.ModelAdmin):
    search_fields = ["email"]
    list_display = ("email",)
    list_per_page = 100
    fields = (
        "email",
        "first_name",
        "last_name",
        "phone",
        "service_user",
    )


admin.site.register(User, ClientModelAdmin)

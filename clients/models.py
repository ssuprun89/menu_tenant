import datetime
import uuid
import re

from django.conf import settings
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django_tenants.postgresql_backend.base import _check_schema_name

from utils.models import UUIDModel


class Client(TenantMixin):
    class TimezoneChoices(models.TextChoices):
        KIYV = "Europe/Kiev", "EET"

    class CurrencyChoices(models.TextChoices):
        UAH = "UAH", "₴"

    name = models.CharField(max_length=100)
    timezone = models.CharField(null=True, choices=TimezoneChoices.choices, default=TimezoneChoices.KIYV)
    currency = models.CharField(null=True, choices=CurrencyChoices.choices, default=CurrencyChoices.UAH)
    created_on = models.DateField(auto_now_add=True)
    code = models.UUIDField(default=uuid.uuid4)
    schema_name = models.CharField(
        max_length=63, unique=True, db_index=True, validators=[_check_schema_name], editable=False
    )
    active = models.BooleanField(default=False, editable=False)

    auto_create_schema = True
    auto_drop_schema = True

    def save(self, verbosity=1, *args, **kwargs):
        super().save(verbosity, *args, **kwargs)
        if not kwargs.get("force_insert"):
            self.domains.filter(is_primary=True).first().save()

    def __str__(self):
        return self.name


class ClientBrand(UUIDModel):
    tenant = models.OneToOneField(
        settings.TENANT_MODEL,
        db_index=True,
        related_name="brand",
        on_delete=models.CASCADE,
    )
    color = models.CharField(max_length=15, default="")
    background_color = models.CharField(max_length=15, default="")
    categories_color = models.CharField(max_length=15, default="")
    font = models.CharField(max_length=30, default="")
    about = models.TextField(null=True, blank=True)


class ClientContact(UUIDModel):

    tenant = models.OneToOneField(
        settings.TENANT_MODEL,
        db_index=True,
        related_name="contact",
        on_delete=models.CASCADE,
    )
    address = models.TextField()
    phone = models.CharField(null=True, blank=True)
    instagram = models.CharField(null=True, blank=True)
    facebook = models.CharField(null=True, blank=True)
    website = models.CharField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)


class Domain(DomainMixin):
    is_primary = models.BooleanField(default=False, db_index=True)

    def save(self, *args, **kwargs):
        # if not self.id or self.tenant.name not in self.domain:
        if not self.id:
            prefix = 0
            name = re.sub(r"[^a-zA-Z0-9-]", "", self.tenant.name).strip("-").lower()
            while True:
                check_name = Domain.objects.filter(domain=f"{name}.{settings.BASE_SITE}").exclude(id=self.id).exists()
                if not check_name:
                    self.domain = f"{name}.{settings.BASE_SITE}"
                    break
                prefix += 1
                name = f"{name}{prefix}"
        super().save(*args, **kwargs)


class ClientsHours(UUIDModel):
    class DateChoice(models.IntegerChoices):
        MONDAY = 1, "Monday"
        TUESDAY = 2, "Tuesday"
        WEDNESDAY = 3, "Wednesday"
        THURSDAY = 4, "Thursday"
        FRIDAY = 5, "Friday"
        SATURDAY = 6, "Saturday"
        SUNDAY = 7, "Sunday"

    tenant = models.ForeignKey(
        settings.TENANT_MODEL,
        db_index=True,
        related_name="hours",
        on_delete=models.CASCADE,
    )
    time_from = models.TimeField(default=datetime.time.min)
    time_by = models.TimeField(default=datetime.time.min)
    day_number = models.IntegerField(choices=DateChoice.choices)


class ClientsStatistic(UUIDModel):
    tenant = models.ForeignKey(
        settings.TENANT_MODEL,
        db_index=True,
        related_name="statistic",
        on_delete=models.CASCADE,
    )
    session_id = models.CharField(max_length=30)
    date_time = models.DateTimeField(auto_now=True)

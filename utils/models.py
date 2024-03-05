import uuid

from django.db import models
from django.utils import timezone


class UUIDModel(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    system_created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True

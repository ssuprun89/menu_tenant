import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    UserManager,
)
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from clients.models import Client
from utils.models import UUIDModel


def generate_code():
    return uuid.uuid4().hex


class User(AbstractBaseUser, PermissionsMixin):
    # DEFAULT FIELDS ------------------------------------------------------------

    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    email = models.EmailField(_("email address"), unique=True)
    password = models.CharField(_("password"), max_length=128, default=generate_code)
    phone = models.CharField(_("phone"), max_length=20)
    service_user = models.BooleanField(default=False)
    invite = models.BooleanField(default=False)

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    # END DEFAULT FIELDS ------------------------------------------------------------

    verify_status = models.BooleanField(
        _("verify status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class UserClient(UUIDModel):
    class UserRole(models.TextChoices):
        OWNER = "owner", "Owner"
        USER = "user", "User"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="user")
    role = models.CharField(max_length=100, choices=UserRole.choices)

    class Meta:
        unique_together = ("user", "role")

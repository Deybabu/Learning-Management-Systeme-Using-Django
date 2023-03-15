from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user.usermanager import (
    AdminManager,
    ProfessorManager,
    StudentManager,
    UserManager
)

STATUS_CHOICE: tuple = (
    ("ADMIN", "ADMIN"),
    ("PROFESSOR", "PROFESSOR"),
    ("STUDENT", "STUDENT")
)


class User(AbstractBaseUser, PermissionsMixin):
    """
    DOCS: User Models
    """

    id = models.UUIDField(
        default=uuid4,
        editable=False,
        blank=False,
        null=False,
        unique=True,
        primary_key=True
    )
    email = models.EmailField(
        _("Email"), max_length=255, blank=False, null=False, unique=True)
    username = models.CharField(
        _("Username"), max_length=255, null=False, blank=False, unique=True)
    first_name = models.CharField(
        _("First Name"), max_length=255, null=True, blank=True)
    last_name = models.CharField(
        _("Last Name"), max_length=255, null=True, blank=True)

    user_status = models.CharField(
        _("User Status"), max_length=100, choices=STATUS_CHOICE, default="ADMIN")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_admin = models.BooleanField(_("Admin Status"), default=False)
    is_active = models.BooleanField(_("Active Status"), default=True)
    is_staff = models.BooleanField(_("Staff Status"), default=False)
    is_superuser = models.BooleanField(_("Superuser Status"), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
    )

    objects = UserManager()
    adminmanager = AdminManager()
    professormanager = ProfessorManager()
    studentmanager = StudentManager()

    class Meta:
        order_with_respect_to = 'created_at'
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self) -> str:
        return f"{self.first_name}"

    def __str__(self) -> str:
        return self.id.hex


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('UserProfile')
        verbose_name_plural = _('UserProfiles')

    def __str__(self) -> str:
        return f"{self.user.get_short_name}-{self.user.id.hex[:5]}"

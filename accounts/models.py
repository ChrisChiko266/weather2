from email.policy import default
from enum import unique
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.utils.translation import gettext_lazy as _

import uuid

class User(AbstractUser, PermissionsMixin):
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(_("Username"), max_length=100, blank=True, unique=True)
    email = models.EmailField(_("Email Address"), blank=True, unique=True)
    name = models.CharField(_("Last Name"), max_length=100, blank=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['email',]

    objects = UserManager()

    def __str__(self) -> str:
        return self.username

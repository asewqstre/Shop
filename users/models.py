from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

class Users(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    groups = []
    user_permissions = []

    username = models.CharField(max_length=30, null=True, blank=False, unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
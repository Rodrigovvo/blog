from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ User base model """
    email = models.EmailField(verbose_name='Email address', unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=30, blank=True)
    last_name = models.CharField(verbose_name='Last name', max_length=30, blank=True)
    is_active = models.BooleanField(verbose_name='Active', default=True)
    is_staff = models.BooleanField(verbose_name='Staff', default=True)
    created_at  = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True
    )
    modified_at = models.DateTimeField(
        verbose_name='Modified at',
        auto_now=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self) -> str:
        """
            Returns the first_name plus the last_name, with a space in between.
        """
        return f'{self.first_name} {self.last_name}'
        
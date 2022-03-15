from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    age = models.IntegerField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['age']

    objects = UserManager()

    def __str__(self):
        return self.email
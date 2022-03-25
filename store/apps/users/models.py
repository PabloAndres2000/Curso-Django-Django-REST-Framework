# Django
from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# Store Utils Models
from store.utils.models import StoreModel


class User(StoreModel, AbstractBaseUser):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    identification_number = models.CharField(
        unique=True,
        max_length=20,
        null=True,
        blank=True
    )
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15)
    ip_address = models.JSONField(default=dict, null=True, blank=True)
    is_staff = models.BooleanField(default=False)

    class Meta:
        app_label = "users"

    def __str__(self):
        return self.first_name

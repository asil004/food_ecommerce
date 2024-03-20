from django.db import models
from base.models import TimeStampModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)


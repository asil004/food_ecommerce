from django.db import models
from base.models import TimeStampModel
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.TextField()
    phone_number = models.CharField(max_length=20)

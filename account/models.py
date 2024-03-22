from django.db import models
from base.models import TimeStampModel
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

=======


class User(AbstractUser):
    address = models.TextField()
    phone_number = models.CharField(max_length=20)
>>>>>>> 31517e9ee4c9466e07829bdf0f7d4b5d2ffd748b

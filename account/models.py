from django.db import models
from base.models import TimeStampModel


class User(TimeStampModel):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.TextField()
    email = models.EmailField()
    phone_number = models.IntegerField(max_length=20)
    password = models.CharField(max_length=30)

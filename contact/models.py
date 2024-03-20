from django.db import models
from base.models import TimeStampModel


class Contact(TimeStampModel):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.first_name

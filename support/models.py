from django.db import models
from base.models import TimeStampModel


class Support(TimeStampModel):
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address} {self.email} {self.phone}"

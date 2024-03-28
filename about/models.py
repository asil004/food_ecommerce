from django.db import models
from base.models import TimeStampModel


class About(TimeStampModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="about/images")

    def __str__(self):
        return self.title


class Positions(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Workers(models.Model):
    first_name = models.CharField(max_length=150)
    position = models.ForeignKey(Positions, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="workers/images", blank=True)
    twitter = models.CharField(max_length=120, blank=True)
    instagram = models.CharField(max_length=120, blank=True)
    linkedin = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.first_name
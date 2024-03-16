from django.db import models
from base.models import TimeStampModel


class About(TimeStampModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="about/images")


class Positions(models.Model):
    name = models.CharField(max_length=100)


class Workers(models.Model):
    first_name = models.CharField(max_length=150)
    position = models.ForeignKey(Positions, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="workers/images")
    twitter = models.CharField(max_length=120)
    instagram = models.CharField(max_length=120)
    linkedin = models.CharField(max_length=120)

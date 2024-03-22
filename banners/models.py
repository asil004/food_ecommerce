from django.db import models
from base.models import TimeStampModel
from products.models import Product


class Banners(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="banners")
    image = models.ImageField(upload_to="banners/images")
    text = models.TextField()

from django.db import models

from base.models import TimeStampModel
from categories.models import Category


class Product(TimeStampModel):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')


class Images(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='product/images')

    def __str__(self):
        return self.product.title


class Color(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='colors')
    color = models.CharField(max_length=50, blank=True, null=True)


class Size(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='size')
    size = models.CharField(max_length=50, blank=True, null=True)


class Stars(TimeStampModel):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name='stars')
    stars = models.IntegerField(max_length=1000, blank=True, null=True)


class Discount(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='discount')
    dis_percentage = models.IntegerField(max_length=1000, blank=True, null=True)
    end_time = models.DateTimeField()

from django.db import models

from base.models import TimeStampModel
from categories.models import Category


class Color(TimeStampModel):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Size(TimeStampModel):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Discount(TimeStampModel):
    dis_percentage = models.IntegerField(blank=True, null=True)
    end_time = models.DateTimeField()

    def __str__(self):
        return self.dis_percentage


class Product(TimeStampModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.PROTECT, null=True, blank=True)
    size = models.ForeignKey(Size, on_delete=models.PROTECT, null=True, blank=True)
    discount = models.ForeignKey(Discount, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.name


class Images(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='product/images')

    def __str__(self):
        return self.product.name


class Stars(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stars')
    stars = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.product.name

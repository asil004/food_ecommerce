from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import User
from base.models import TimeStampModel
from products.models import Product


class ProductBasket(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField()
    sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        self.sum = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.name} * {self.quantity} = {self.sum}"


class Basket(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_basket')
    # product_basket = models.ForeignKey(ProductBasket, on_delete=models.CASCADE, related_name='product_basket')
    sum = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.sum}"

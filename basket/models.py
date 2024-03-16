from django.db import models
from base.models import TimeStampModel
from products.models import Product


class ProductBasket(TimeStampModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    quantity = models.PositiveIntegerField()
    sum = models.FloatField()

    def __str__(self):
        return f"{self.product.name} * {self.quantity} = {self.sum}"


class Basket(TimeStampModel):
    product_basket = models.ForeignKey(ProductBasket, on_delete=models.CASCADE, related_name='product_basket')
    sum = models.FloatField()

    def __str__(self):
        return f"{self.product_basket} = {self.sum}"

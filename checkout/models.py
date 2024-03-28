from django.db import models
from basket.models import Basket, ProductBasket
from account.models import User
from base.models import TimeStampModel
from products.models import Product, Size, Color


class BillingDetails(TimeStampModel):
    first_name = models.CharField(max_length=150)
    company_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    apartment = models.CharField(max_length=100)
    town_city = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.first_name


bank_card = (
    ('K', 'Karta'),
    ('N', 'Naxt'),
)


class Checkout(TimeStampModel):
    cupon_code = models.CharField(max_length=100, null=True, blank=True)
    is_checkout = models.BooleanField(default=False)
    card_number = models.CharField(null=True, blank=True, max_length=20)
    card_date = models.CharField(null=True, blank=True, max_length=5)
    payment_type = models.CharField(max_length=1, choices=bank_card)

    class Meta:
        abstract = True


class CheckoutBasket(Checkout):
    product_basket = models.ManyToManyField(ProductBasket, related_name='product_basket')
    billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE, related_name='CheckoutBasket')
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='CheckoutBasket')

    def __str__(self):
        return str(self.id)



class ProductCheckout(Checkout):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_checkout')
    quantity = models.PositiveSmallIntegerField(default=0)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE, related_name='Checkoutbilling')
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='CheckoutProduct')

    def __str__(self):
        return str(self.id)

from django.db import models
from basket.models import Basket

"""
Rustam: 

1: Checkout
2: Order
3: Contact
"""


class BillingDetails(models.Model):
    first_name = models.CharField(max_length=50)
    company_name = models.CharField(50)
    address = models.CharField(100)
    apartment = models.CharField()
    town_city = models.CharField()
    phone_number = models.CharField(max_length=13)
    email = models.CharField(max_length=30)


class Checkout(models.Model):
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='Checkout')
    cupon_code = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('K', 'Karta'),
        ('N', 'Naxt'),
    )
    payemnt_type = models.CharField(max_length=1, choices=GENDER_CHOICES)
    billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE, related_name='Checkout')

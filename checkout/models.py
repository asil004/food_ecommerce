from django.db import models
from basket.models import Basket
from account.models import User
from base.models import TimeStampModel


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


class Checkout(TimeStampModel):
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='Checkout')
    cupon_code = models.CharField(max_length=100)
    GENDER_CHOICES = (
        ('K', 'Karta'),
        ('N', 'Naxt'),
    )
    payment_type = models.CharField(max_length=1, choices=GENDER_CHOICES)
    billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE, related_name='Checkout')
    account = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Checkout')

    def __str__(self):
        return self.basket_id

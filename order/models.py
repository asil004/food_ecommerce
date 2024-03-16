from django.db import models
from basket.models import Basket
from checkout.models import BillingDetails
from account import Account


class Order(models.Model):
    basket_id = models.ForeignKey(Basket, on_delete=models.CASCADE, related_name='Order')
    GENDER_CHOICES = (
        ('K', 'Karta'),
        ('N', 'Naxt'),
    )
    payemnt_type = models.CharField(max_length=1, choices=GENDER_CHOICES)
    billing_details = models.ForeignKey(BillingDetails, on_delete=models.CASCADE, related_name='Order')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Order')

    def __str__(self):
        return self.payemnt_type

from checkout.serializers import BillingDetailsSerializers
from .models import Order
from rest_framework import serializers


class OrderSerializers(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()

    class Meta:
        model = Order
        fields = ['billing_details', 'payment_type', ]

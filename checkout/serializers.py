from basket.models import ProductBasket
from .models import Checkout, BillingDetails
from rest_framework import serializers


class BillingDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BillingDetails
        exclude = ['created_at', 'updated_at']


class CheckoutSerializers(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()

    class Meta:
        model = Checkout
        fields = ['billing_details', 'cupon_code', 'payment_type', 'card_number', 'card_date']

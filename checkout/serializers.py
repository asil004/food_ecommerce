from basket.models import ProductBasket
from basket.serializers import ProductBasketSerializer
from products.models import Product
from products.serializers import ProductSerializer
from .models import Checkout, BillingDetails, bank_card, CheckoutBasket, ProductCheckout
from rest_framework import serializers
from products.models import *


class BillingDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BillingDetails
        exclude = ['created_at', 'updated_at']


class CheckoutSerializers(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()

    class Meta:
        model = CheckoutBasket
        fields = ['id','billing_details', 'cupon_code', 'payment_type', 'card_number', 'card_date']


class CheckoutProductSerializers(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()

    class Meta:
        model = ProductCheckout
        fields = ['id','billing_details', 'cupon_code', 'payment_type', 'card_number', 'card_date',
                  'quantity', 'total_sum']


class MyOrdersSerializer(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()
    product_basket = ProductBasketSerializer(many=True)
    payment_type = serializers.ChoiceField(
        read_only=True, choices=bank_card
    )

    class Meta:
        model = CheckoutBasket
        exclude = ['created_at', 'updated_at', 'cupon_code', 'card_number', 'card_date', 'account']


class MyOrderProductSerializer(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()
    product = ProductSerializer()
    payment_type = serializers.ChoiceField(
        read_only=True, choices=bank_card
    )

    class Meta:
        model = ProductCheckout
        exclude = ['created_at', 'updated_at', 'cupon_code', 'card_number', 'card_date', 'account']
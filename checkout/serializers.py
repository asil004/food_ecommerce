from basket.models import ProductBasket
from basket.serializers import ProductBasketSerializer
from .models import Checkout, BillingDetails, bank_card
from rest_framework import serializers


class BillingDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BillingDetails
        exclude = ['created_at', 'updated_at']


class CheckoutSerializers(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()
    payment_type = serializers.MultipleChoiceField(choices=bank_card)

    class Meta:
        model = Checkout
        fields = ['billing_details', 'cupon_code', 'payment_type', 'card_number', 'card_date']


class MyOrdersSerializer(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()
    product_basket = ProductBasketSerializer(many=True)
    payment_type = serializers.ChoiceField(
        source='get_payment_type_display', read_only=True, choices=bank_card
    )

    class Meta:
        model = Checkout
        exclude = ['created_at', 'updated_at', 'cupon_code', 'card_number', 'card_date', 'account']

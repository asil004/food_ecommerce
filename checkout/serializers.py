from basket.models import ProductBasket
from basket.serializers import ProductBasketSerializer
from products.models import Product
from .models import Checkout, BillingDetails, bank_card, CheckoutBasket, CheckoutProduct
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
        fields = ['billing_details', 'cupon_code', 'payment_type', 'card_number', 'card_date']


class CheckoutProductSerializers(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()

    class Meta:
        model = CheckoutProduct
        fields = ['billing_details', 'cupon_code', 'payment_type', 'card_number', 'card_date', 'color', 'size',
                  'quantity']


class MyOrdersSerializer(serializers.ModelSerializer):
    billing_details = BillingDetailsSerializers()
    product_basket = ProductBasketSerializer(many=True)
    payment_type = serializers.ChoiceField(
        read_only=True, choices=bank_card
    )

    class Meta:
        model = CheckoutBasket
        exclude = ['created_at', 'updated_at', 'cupon_code', 'card_number', 'card_date', 'account']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ['created_at', 'updated_at']


class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        exclude = ['created_at', 'updated_at']


class ColorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        exclude = ['created_at', 'updated_at']


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        exclude = ['created_at', 'updated_at']

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ['created_at', 'updated_at']


class billingDetailscheckutSerializers(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    color = ColorsSerializer(many=True)
    size = SizesSerializer(many=True)
    stars = StarsSerializer(many=True)


    class Meta:
        model = Product
        fields = ["id", "name", "slug", "price", "quantity", "description", "category", "color", "size",
                  "images", "stars", "discount"]

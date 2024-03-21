from rest_framework import serializers

from .models import Product, ProductBasket, Basket


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['created_at', 'updated_at']


class ProductBasketSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductBasket
        fields = ['user', 'id', 'product', 'quantity', 'sum']


class ProductBasketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBasket
        fields = ['product']

    def create(self, validated_data):
        validated_data['quantity'] = 1
        return ProductBasket.objects.create(**validated_data)


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        exclude = ['created_at', 'updated_at']

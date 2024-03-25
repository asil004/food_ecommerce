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


class ProductBasketPlusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBasket
        fields = ['id']

    def create(self, validated_data):
        request = self.context.get('request')
        product_basket = ProductBasket.objects.get(pk=request.data['id'])
        product_basket.quantity += 1
        product_basket.save()
        return product_basket


class ProductBasketMinusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBasket
        fields = ['id']

    def create(self, validated_data):
        request = self.context.get('request')
        product_id = request.data['id']
        product_basket = ProductBasket.objects.get(id=product_id)

        if product_basket.quantity == 1:
            product_basket.delete()
        else:
            product_basket.quantity -= 1
            product_basket.save()

        return product_basket


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        exclude = ['created_at', 'updated_at']

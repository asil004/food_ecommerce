from rest_framework import serializers

from categories.models import Category
from .models import *


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        exclude = ['created_at', 'updated_at']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        exclude = ['created_at', 'updated_at']


class StarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stars
        exclude = ['created_at', 'updated_at']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class ProductCategorySerializers(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    stars = StarsSerializer(many=True)
    discount = DiscountSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "price", "category", "discount", "images", "stars"]


class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    stars = StarsSerializer(many=True)
    discount = DiscountSerializer()
    color = ColorSerializer()

    class Meta:
        model = Product
        fields = ["id", "name", "slug", "price", "quantity", "description", "color", "size", "category", "discount",
                  "images", "stars"]

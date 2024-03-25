from rest_framework import serializers
from .models import Wishlist
from account.models import User
from account.serializers import UserSerializers
from products.serializers import ProductSerializers


class WishlistGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        exclude = ['created_at', 'updated_at']


class WishlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = ["wishlist_user", "wishlist_pro"]

    # def __init__(self, *args, **kwargs):
    #     super(WishlistSerializer, self).__init__(*args, **kwargs)
    #
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     response['user'] = UserSerializers(instance.user).data
    #     response['product'] = ProductSerializers(instance.product).data
    #     return response

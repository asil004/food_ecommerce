from .models import Checkout
from rest_framework import serializers


class CheckoutSerializers(serializers.ModelSerializer):
    class Meta:
        model = Checkout
        fields = "__all__"

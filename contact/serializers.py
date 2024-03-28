from .models import Contact
from rest_framework import serializers


class ContactSerializers(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=20)
    message = serializers.CharField(max_length=255)

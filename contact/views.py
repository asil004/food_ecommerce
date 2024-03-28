from django.shortcuts import render
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializers


class ContactListAPIView(generics.ListAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializers
from rest_framework import generics


class OrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers

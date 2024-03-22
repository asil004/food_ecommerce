from django.shortcuts import render
from rest_framework import generics
from wishlist.serializers import WishlistSerializer
from wishlist.models import Wishlist


class WishlistViewSet(generics.ListAPIView):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer

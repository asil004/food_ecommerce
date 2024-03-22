from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from categories.serializers import CategorySerializer
from categories.models import Category


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


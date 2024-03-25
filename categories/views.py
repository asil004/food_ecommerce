from django.shortcuts import render
from rest_framework import generics, viewsets
from .serializers import CategorySerializer
from .models import Category
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


# Create your views here.

class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

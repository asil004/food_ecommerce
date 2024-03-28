from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import ProductCategorySerializers, ProductSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from datetime import datetime, timedelta
import random
from django.utils import timezone


class ProductCategoryViewSet(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='category_slug',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Category slug',
                required=True
            ),
        ]
    )
    def get(self, request):
        category_slug = request.query_params.get('category_slug')
        if category_slug:
            try:
                category = Category.objects.get(slug=category_slug)
                products = Product.objects.filter(category=category)
                serializer = ProductCategorySerializers(products, many=True)
                return Response(serializer.data)
            except Category.DoesNotExist:
                return Response({"message": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Category slug is required"}, status=status.HTTP_400_BAD_REQUEST)


class Flashsalesproduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            current_time = datetime.now()
            end_time_threshold = current_time + timedelta(days=10)
            products = Product.objects.filter(discount__end_time__lte=end_time_threshold)
            serializer = ProductCategorySerializers(products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)


class BestSellingProduct(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            all_products = Product.objects.all()
            random_products = list(all_products)
            random.shuffle(random_products)
            num_products_to_display = 10
            selected_products = random_products[:num_products_to_display]
            serializer = ProductCategorySerializers(selected_products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"message": "The request was sent incorrectly"}, status.HTTP_400_BAD_REQUEST)


class OurProducts(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            end_date = timezone.now()
            start_date = end_date - timezone.timedelta(days=10)
            products = Product.objects.filter(created_at__range=(start_date, end_date))
            serializer = ProductCategorySerializers(products, many=True)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"message": "The request was sent incorrectly"}, status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='slug',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Product Slug',
                required=True
            ),
        ]
    )
    def get(self, request):

        slug = request.query_params.get('slug')

        if not slug:
            return Response({"message": "Product Slug is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            product = get_object_or_404(Product, slug=slug)
            serializer = ProductSerializer(product)
            category_slug = product.category.slug
            similar_products = Product.objects.filter(category__slug=category_slug).exclude(id=product.id)[:4]
            similar_products_serializer = ProductSerializer(similar_products, many=True)
            response_data = {
                "product_details": serializer.data,
                "similar_products": similar_products_serializer.data
            }

            return Response(response_data)
        except Product.DoesNotExist:
            return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

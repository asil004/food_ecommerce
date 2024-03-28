from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from basket.models import ProductBasket
from .models import Checkout, BillingDetails
from .serializers import CheckoutSerializers, BillingDetailsSerializers, MyOrdersSerializer
from products.models import Product
from .serializers import billingDetailscheckutSerializers
from django.db import transaction
from django.db.models import Sum, F

class CheckoutCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=CheckoutSerializers)
    def post(self, request):
        user = self.request.user
        serializer = CheckoutSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Extract and validate billing details
        billing_details_data = serializer.validated_data.pop('billing_details', None)
        if not billing_details_data:
            raise ValidationError("Billing details are required")

        bd_serializer = BillingDetailsSerializers(data=billing_details_data)
        bd_serializer.is_valid(raise_exception=True)
        billing_details = bd_serializer.save()
        product_basket = ProductBasket.objects.filter(user=user)
        checkout = Checkout.objects.filter(account=user, is_checkout=False).first()
        if not checkout:
            checkout = Checkout.objects.create(account=user, billing_details=billing_details,
                                               **serializer.validated_data)
        for pb in product_basket:
            checkout.product_basket.add(pb)

        return Response({}, status=status.HTTP_201_CREATED)


class MyOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        checkout = Checkout.objects.filter(account=user)
        serializer = MyOrdersSerializer(checkout, many=True)
        if checkout:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Orders Not fount"}, status=status.HTTP_204_NO_CONTENT)


class ProductDetailsCheckoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Product name',
                required=True
            ),
        ]
    )
    def get(self, request):
        name = request.query_params.get('name')
        try:
            products = Product.objects.filter(name=name)
        except Product.DoesNotExist:
            return Response({"error": "Ushbu nomga ega bo'lgan mahsulot topilmadi"}, status=status.HTTP_404_NOT_FOUND)
        serializer = billingDetailscheckutSerializers(products, many=True)
        return Response({"data": serializer.data})


class CheckoutSold(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='color_slug',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='color slug',
                required=True
            ),
            openapi.Parameter(
                name='size_slug',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='size slug',
                required=True
            ),
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Product name',
                required=True
            ),
        ]
    )
    def get(self, request, quantity):
        name = request.query_params.get('name')
        color_slug = request.query_params.get('color_slug')
        size_slug = request.query_params.get('size_slug')
        try:
            products = Product.objects.filter(
                name=name, color__slug=color_slug, size__slug=size_slug
            )
        except Product.DoesNotExist:
            return Response(
                {"error": "Ushbu nom, rang yoki o'lchov nomiga ega bo'lgan mahsulot topilmadi"},
                status=404,
            )

        if not products.exists():
            return Response(
                {"error": "Ushbu nom, rang yoki o'lchov nomiga ega bo'lgan mahsulot topilmadi"},
                status=404,
            )
        total_sum = products.aggregate(total_price=Sum(F('price') * quantity))['total_price']
        serializer = billingDetailscheckutSerializers(products, many=True)
        return Response({"result": serializer.data, "total_sum": total_sum}, status=200)

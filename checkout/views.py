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
from .serializers import CheckoutSerializers, BillingDetailsSerializers


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

from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from basket.models import ProductBasket
from products.models import Product

from .models import Checkout, BillingDetails, CheckoutBasket, ProductCheckout
from .serializers import CheckoutSerializers, BillingDetailsSerializers, MyOrdersSerializer, CheckoutProductSerializers, \
    MyOrderProductSerializer

from django.db import transaction


# checkout
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
        checkout = CheckoutBasket.objects.filter(account=user, is_checkout=False).first()
        if not checkout:
            checkout = CheckoutBasket.objects.create(account=user, billing_details=billing_details,
                                                     **serializer.validated_data)
        else:
            raise ValidationError("This product already in checkout and not payed!")
        for pb in product_basket:
            checkout.product_basket.add(pb)

        return Response({'message': 'Checkout successfully created.'}, status=status.HTTP_201_CREATED)


class ProductCheckoutCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=CheckoutProductSerializers)
    def post(self, request, product_slug):
        user = request.user
        product = Product.objects.get(slug=product_slug)

        serializer = CheckoutProductSerializers(data=request.data)

        if serializer.is_valid():
            billing_details_data = serializer.validated_data.pop('billing_details', None)
            if not billing_details_data:
                raise ValidationError("Billing details are required")

            bd_serializer = BillingDetailsSerializers(data=billing_details_data)
            bd_serializer.is_valid(raise_exception=True)
            billing_details = bd_serializer.save()

            checkout = ProductCheckout.objects.filter(account=user, is_checkout=False).first()
            if not checkout:
                ProductCheckout.objects.create(account=user, product=product, billing_details=billing_details,**serializer.validated_data)


            else:
                raise ValidationError("This product already in checkout and not payed!")
            return Response({'message': 'Checkout successfully created.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MyOrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        checkout = CheckoutBasket.objects.filter(account=user)
        checkout_p = ProductCheckout.objects.filter(account=user)
        # checkout_p = get_object_or_404(ProductCheckout,account=user)
        print(checkout_p)
        serializer = MyOrdersSerializer(checkout, many=True)
        serializer_p = MyOrderProductSerializer(checkout_p, many=True)
        if checkout:
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif checkout_p:
            return Response(serializer_p.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Orders Not found!"}, status=status.HTTP_204_NO_CONTENT)

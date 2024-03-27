from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from basket.models import ProductBasket
from products.models import Product
from .models import Checkout
from .serializers import CheckoutSerializers, BillingDetailsSerializers, MyOrdersSerializer


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
        checkout = Checkout.objects.filter(account=user, is_checkout=False).first()
        if not checkout:
            checkout = Checkout.objects.create(account=user, billing_details=billing_details,
                                               **serializer.validated_data)
        for pb in product_basket:
            checkout.product_basket.add(pb)

        return Response({'message': 'Checkout successfully created.'}, status=status.HTTP_201_CREATED)


class ProductCheckoutCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=CheckoutSerializers)
    def post(self, request, pk):
        user = request.user
        product = Product.objects.get(pk=pk)

        serializer = CheckoutSerializers(data=request.data)

        if serializer.is_valid():
            billing_details_data = serializer.validated_data.pop('billing_details', None)
            if not billing_details_data:
                raise ValidationError("Billing details are required")

            bd_serializer = BillingDetailsSerializers(data=billing_details_data)
            bd_serializer.is_valid(raise_exception=True)
            billing_details = bd_serializer.save()

            checkout = Checkout.objects.filter(account=user, is_checkout=False).first()
            if not checkout:
                Checkout.objects.create(account=user, billing_details=billing_details, product=product,
                                        **serializer.validated_data)

            return Response({'message': 'Checkout successfully created.'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

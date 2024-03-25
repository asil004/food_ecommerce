from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .serializers import ProductBasketSerializer, ProductBasketCreateSerializer, BasketSerializer, \
    ProductBasketPlusSerializer
from .models import ProductBasket, Basket


def update_basket_sum(user):
    total_sum = ProductBasket.objects.filter(user=user).aggregate(total_sum=Sum('sum'))['total_sum']
    basket, _ = Basket.objects.get_or_create(user=user)
    basket.sum = total_sum or 0.0
    basket.save()


class ProductBasketListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        product_baskets = ProductBasket.objects.filter(user__id=user_id)
        serializer = ProductBasketSerializer(product_baskets, many=True)
        return Response(serializer.data)


class ProductBasketCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'product': openapi.Schema(type=openapi.TYPE_INTEGER, description='Product ID'),
            }
        )
    )
    def post(self, request):
        serializer = ProductBasketCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            update_basket_sum(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductBasketDestroyAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        try:
            product_basket = ProductBasket.objects.get(user=request.user, id=id)
            product_basket.delete()
            update_basket_sum(request.user)
            return Response("Product Basket deleted successfully.", status=status.HTTP_204_NO_CONTENT)
        except ProductBasket.DoesNotExist:
            return Response("Product Basket not found for the current user.", status=status.HTTP_404_NOT_FOUND)


# plus and minus
class ProductBasketPlusAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProductBasketPlusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            update_basket_sum(request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BasketListView(ListAPIView):
    serializer_class = BasketSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Basket.objects.filter(user=user)

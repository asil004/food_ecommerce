from django.db.models import Sum
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .serializers import ProductBasketSerializer, ProductBasketCreateSerializer, BasketSerializer
from .models import ProductBasket, Basket


def update_basket_sum(user):
    total_sum = ProductBasket.objects.filter(user=user).aggregate(total_sum=Sum('sum'))['total_sum']
    basket, _ = Basket.objects.get_or_create(user=user)
    basket.sum = total_sum or 0.0
    basket.save()


class ProductBasketListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        product_baskets = ProductBasket.objects.filter(user__id=user_id)
        serializer = ProductBasketSerializer(product_baskets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductBasketCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            update_basket_sum(request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        try:
            product_basket = ProductBasket.objects.get(user=request.user, pk=pk)
            product_basket.delete()
            update_basket_sum(request.user)
            return Response("Product Basket deleted successfully.", status=204)
        except ProductBasket.DoesNotExist:
            return Response("Product Basket not found for the current user.", status=404)


class BasketListView(ListAPIView):
    serializer_class = BasketSerializer

    def get_queryset(self):
        user = self.request.user
        return Basket.objects.filter(user=user)

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from .serializers import WishlistGetSerializer, WishlistCreateSerializer
from .models import Wishlist
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView


# Create your views here.


class GetWishlist(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id
        user_wishlist = Wishlist.objects.filter(user_id=user_id)
        serializer = WishlistGetSerializer(user_wishlist, many=True)
        return Response(serializer.data)


class CreateWishlist(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = WishlistCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class DeleteWishlist(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        try:
            delete_wishlist = Wishlist.objects.get(user=request.user)
            delete_wishlist.delete()
            return Response("Wishlist deleted successfully.", status=204)
        except Wishlist.DoesNotExist:
            return Response("Wishlist not found for the current user.", status=404)

# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def check_in_wishlist(request):
#     if request.method == "POST":
#         product_id = request.POST.get('product')
#         user_id = request.POST.get('user')
#         check_wishlist = Wishlist.objects.filter(product_id=product_id, user_id=user_id).count()
#         if check_wishlist == 0:
#             wishlist_item = Wishlist.objects.create(product_id=product_id, user_id=user_id)
#             wishlist_item.save()
#             # success: True bo'lsa yurakcha qizil boladi
#             msg = {'success': True, 'message': 'Mahsulot "Wishlist" ro\'yxatiga muvaffaqiyatli qo\'shildi.'}
#         else:
#             # success : True bu mahsulot databaseda bo'lganligi sababli yurakcha yana qizil bolib turishi uchun
#             msg = {'success': True, 'message': 'Mahsulot allaqachon "Wishlist" ro\'yxatida mavjud.'}
#         return JsonResponse(msg)
#
#
# @csrf_exempt
# @permission_classes([IsAuthenticated])
# def delete_wishlist(request):
#     if request.method == "POST":
#         product_id = request.POST.get('product')
#         user_id = request.POST.get('user')
#         wishlist_item = Wishlist.objects.filter(product_id=product_id, user_id=user_id).first()
#         if wishlist_item is not None:
#             wishlist_item.delete()
#             msg = {'success': True, 'message': 'Mahsulot "Wishlist" ro\'yxatiga muvaffaqiyatli o\'chirildi.'}
#         else:
#             msg = {'success': False, 'message': 'Bu mahsulot bu foyfalanuvchini ro\'yxatida mavjud emas'}
#         return JsonResponse(msg)

from django.urls import path
from .views import BasketListView, ProductBasketListAPIView, ProductBasketCreateAPIView, ProductBasketDestroyAPIView, \
    ProductBasketPlusAPIView, ProductBasketMinusAPIView

urlpatterns = [
    path('product-baskets/', ProductBasketListAPIView.as_view(), name='product_basket'),
    path('product-baskets-add/', ProductBasketCreateAPIView.as_view(), name='product_basket_create'),
    path('product-baskets-plus/', ProductBasketPlusAPIView.as_view(), name='product_basket_plus'),
    path('product-baskets-minus/', ProductBasketMinusAPIView.as_view(), name='product_basket_minus'),
    path('product-baskets-delete/<int:id>', ProductBasketDestroyAPIView.as_view(), name='product_basket_delete'),
    path('basket/', BasketListView.as_view())
]

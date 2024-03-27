from django.urls import path, include
from .views import BasketListView, ProductBasketListAPIView, ProductBasketCreateAPIView, ProductBasketDestroyAPIView, \
    ProductBasketPlusAPIView, ProductBasketMinusAPIView

urlpatterns = [
    path('product-baskets/', include([
        path('', ProductBasketListAPIView.as_view(), name='product_basket'),
        path('add/', ProductBasketCreateAPIView.as_view(), name='product_basket_create'),
        path('plus/', ProductBasketPlusAPIView.as_view(), name='product_basket_plus'),
        path('minus/', ProductBasketMinusAPIView.as_view(), name='product_basket_minus'),
        path('delete/<int:id>', ProductBasketDestroyAPIView.as_view(), name='product_basket_delete'),
    ])),
    path('basket/', BasketListView.as_view())
]

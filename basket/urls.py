from django.urls import path
from .views import ProductBasketListCreateAPIView, BasketListView, ProductBasketDeleteAPIView

urlpatterns = [
    path('product_baskets/', ProductBasketListCreateAPIView.as_view(), name='product_basket_list_create'),
    path('product_baskets/<int:pk>/', ProductBasketDeleteAPIView.as_view(), name='product_basket_delete'),
    path('basket/', BasketListView.as_view())
]

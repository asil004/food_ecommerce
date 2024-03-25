from django.urls import path
from .views import ProductBasketListCreateAPIView, BasketListView

urlpatterns = [
    path('product_baskets/', ProductBasketListCreateAPIView.as_view(), name='product_basket'),
    path('product_baskets-add/<int:pk>', ProductBasketListCreateAPIView.as_view(), name='product_basket_add'),
    path('product_baskets-delete/<int:pk>', ProductBasketListCreateAPIView.as_view(), name='product_basket_delete'),
    path('basket/', BasketListView.as_view())
]

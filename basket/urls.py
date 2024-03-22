from django.urls import path
from .views import ProductBasketListCreateAPIView, BasketListView

urlpatterns = [
    path('product_baskets/', ProductBasketListCreateAPIView.as_view(), name='product_basket'),
    path('basket/', BasketListView.as_view())
]

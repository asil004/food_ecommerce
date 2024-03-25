from django.urls import path

from order.views import OrderListAPIView

urlpatterns = [
    path('order_list/', OrderListAPIView.as_view())
]

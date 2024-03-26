from django.urls import path

from .views import OrderListCreateView

urlpatterns = [
    path('order-create/', OrderListCreateView.as_view()),
]

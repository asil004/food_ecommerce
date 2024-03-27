from django.urls import path

from .views import CheckoutCreateView, MyOrdersView

urlpatterns = [
    path('checkout-create/', CheckoutCreateView.as_view()),
    path('my-orders/', MyOrdersView.as_view()),
]

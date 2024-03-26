from django.urls import path

from .views import (CheckoutCreateView)

urlpatterns = [
    path('checkout-create/', CheckoutCreateView.as_view()),

]

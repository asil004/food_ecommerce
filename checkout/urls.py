from django.urls import path

from .views import CheckoutListCreateView, CheckoutRetrieveUpdateDestroyView

urlpatterns = [
    path('checkout-create/', CheckoutListCreateView.as_view()),
    path('checkout-update/', CheckoutRetrieveUpdateDestroyView.as_view()),
]

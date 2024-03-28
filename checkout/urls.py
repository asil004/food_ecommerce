from django.urls import path

from .views import CheckoutCreateView, MyOrdersView, ProductDetailsCheckoutView, CheckoutSold

urlpatterns = [
    path('checkout-create/', CheckoutCreateView.as_view()),
    path('my-orders/', MyOrdersView.as_view()),
    path('product-detail-checkout/', ProductDetailsCheckoutView.as_view()),
    path('detail-checkout/<int:quantity>', CheckoutSold.as_view())
]

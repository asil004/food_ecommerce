from django.urls import path, include

from .views import CheckoutCreateView, MyOrdersView, ProductCheckoutCreateView

urlpatterns = [
    path('checkout/', include([
        path('basket-create/', CheckoutCreateView.as_view()),
        path('product-create/<int:pk>', ProductCheckoutCreateView.as_view()),
    ])),
    path('my-orders/', MyOrdersView.as_view()),
]

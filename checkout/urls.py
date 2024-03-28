from django.urls import path, include

from .views import CheckoutCreateView, MyOrdersView, ProductCheckoutCreateView

app_name = 'checkout'

urlpatterns = [
    path('checkout/', include([
        path('basket-create/', CheckoutCreateView.as_view()),
        path('product-create/<slug:product_slug>', ProductCheckoutCreateView.as_view()),
    ])),
    path('my-orders/', MyOrdersView.as_view()),
]

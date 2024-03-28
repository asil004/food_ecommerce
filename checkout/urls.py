from django.urls import path, include


from .views import CheckoutCreateView, MyOrdersView, ProductDetailsCheckoutView, CheckoutSold



urlpatterns = [
    path('checkout/', include([
        path('basket-create/', CheckoutCreateView.as_view()),
        path('product-create/<int:pk>', ProductCheckoutCreateView.as_view()),
    ])),
    path('my-orders/', MyOrdersView.as_view()),
    path('product-detail-checkout/', ProductDetailsCheckoutView.as_view()),
    path('detail-checkout/<int:quantity>', CheckoutSold.as_view())
]

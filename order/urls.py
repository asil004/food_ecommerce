from django.urls import path

from .views import OrderCreateView, OrderPutView, OrderPostView, OrderDeleteView

urlpatterns = [
    path('order-create/', OrderCreateView.as_view()),
    path('order-post/', OrderPostView.as_view()),
    path('order-put/<int:pk>/', OrderPutView.as_view()),
    path('order-delete/<int:pk>/', OrderDeleteView.as_view()),
]

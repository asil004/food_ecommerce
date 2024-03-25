from django.urls import path
from .views import UserListAPIView

urlpatterns = [
    path('test/', UserListAPIView.as_view())
]

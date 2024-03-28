from django.urls import path
from .views import ContactListAPIView

urlpatterns = [
    path('contact/', ContactListAPIView.as_view())
]

from django.urls import path
from .views import ContactListAPIView

urlpatterns = [
    path('contact_list_apiview/', ContactListAPIView.as_view())
]

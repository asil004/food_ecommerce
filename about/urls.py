from django.urls import path
from .views import AboutListAPIView, WorkersListAPIView

urlpatterns = [
    path('about', AboutListAPIView.as_view(), name='about'),
    path('about/workers', WorkersListAPIView.as_view(), name='workers')
]
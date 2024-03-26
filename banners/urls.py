from django.urls import path

from .views import BannerListAPIView

urlpatterns = [
    path('banner', BannerListAPIView.as_view(), name='banner')
]
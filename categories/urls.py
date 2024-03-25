from django.urls import path

from .views import *

urlpatterns = [
    path('category/', CategoryViewSet.as_view(), name='category_name')
]

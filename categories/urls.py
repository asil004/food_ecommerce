from django.urls import path, include
from categories.views import *

urlpatterns = [
    path('category/',CategoryViewSet.as_view())
]

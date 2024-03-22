from django.urls import path, include
from wishlist.views import *

urlpatterns = [
    path('wishlist/',WishlistViewSet.as_view())
]
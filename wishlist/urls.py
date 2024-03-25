from django.urls import path
from .views import *

urlpatterns = [
    path('GetWishlist/', GetWishlist.as_view(), name='Get_Wishlist'),
    path('CreateWishlist/<int:pk>', CreateWishlist.as_view(), name='Create_Wishlist'),
    path('DeleteWishlist/<int:pk>', DeleteWishlist.as_view(), name='Delete_Wishlist')
]

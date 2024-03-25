from django.urls import path
from .views import *

urlpatterns = [
    path('getwishlist/', GetWishlist.as_view(), name='Get_Wishlist'),
    path('createwishlist/', CreateWishlist.as_view(), name='Create_Wishlist'),
    path('deletewishlist/<int:id>', DeleteWishlist.as_view(), name='Delete_Wishlist')
]

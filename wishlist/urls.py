from django.urls import path, include
from .views import *

urlpatterns = [
    path('wishlist/', include([
        path('', GetWishlist.as_view(), name='Get_Wishlist'),
        path('create/', CreateWishlist.as_view(), name='Create_Wishlist'),
        path('delete/<int:id>', DeleteWishlist.as_view(), name='Delete_Wishlist')
    ]))

]

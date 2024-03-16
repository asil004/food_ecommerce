from django.db import models
from base.models import TimeStampModel
from products.models import Product
from account.models import User


class Wishlist(TimeStampModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlists")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_user")

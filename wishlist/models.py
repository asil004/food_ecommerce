from django.db import models
from base.models import TimeStampModel
from products.models import Product
from account.models import User


class Wishlist(TimeStampModel):
    wishlist_pro = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlists_pro",default=True)
    wishlist_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_user",default=True
                                      )

    def __str__(self):
        return f"{self.wishlist_pro.name} - {self.wishlist_user.username}"

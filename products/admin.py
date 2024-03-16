from django.contrib import admin
from .models import Product, Images, Color, Size, Stars

admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Stars)

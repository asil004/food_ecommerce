from django.contrib import admin

from basket.models import ProductBasket, Basket

admin.site.register(Basket)
admin.site.register(ProductBasket)

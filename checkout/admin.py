from django.contrib import admin
from .models import CheckoutBasket, CheckoutProduct, BillingDetails

admin.site.register(CheckoutBasket)
admin.site.register(CheckoutProduct)
admin.site.register(BillingDetails)

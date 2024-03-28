from django.contrib import admin
from .models import CheckoutBasket, ProductCheckout, BillingDetails

admin.site.register(CheckoutBasket)
admin.site.register(ProductCheckout)
admin.site.register(BillingDetails)

from django.contrib import admin
from .models import Checkout, BillingDetails

admin.site.register(Checkout)
admin.site.register(BillingDetails)


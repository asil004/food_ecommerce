from django.contrib import admin
from .models import Product, Images, Color, Size, Stars, Discount


class ImagesAdmin(admin.TabularInline):
    model = Images


class ColorAdmin(admin.TabularInline):
    model = Color
    extra = 1


class SizeAdmin(admin.TabularInline):
    model = Size
    extra = 1


class StarsAdmin(admin.TabularInline):
    model = Stars
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin, ColorAdmin, SizeAdmin, StarsAdmin]


admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Stars)
admin.site.register(Discount)

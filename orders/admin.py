from django.contrib import admin
from .models import Cart, CartProductMapping


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartProductMapping)
class CartProductMappingAdmin(admin.ModelAdmin):
    pass

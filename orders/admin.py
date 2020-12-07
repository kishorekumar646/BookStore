from django.contrib import admin
from .models import Cart, CartProductMapping
from django.utils.translation import ugettext_lazy as _
from .forms import OrderUserForm


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Cart info'), {'fields': ('user', 'product', 'is_ordered')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('product','user','is_ordered',)
    list_filter = ('is_ordered','user')
    search_fields = ('product','user')
    readonly_fields = ('created_at', 'modified_at',)

@admin.register(CartProductMapping)
class CartProductMappingAdmin(admin.ModelAdmin):
    form = OrderUserForm
    fieldsets = (
        (_('Order info'), {'fields': ('user', 'items')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('user',)
    list_filter = ('created_at', 'modified_at',)
    search_fields = ('user',)
    readonly_fields = ('created_at', 'modified_at',)
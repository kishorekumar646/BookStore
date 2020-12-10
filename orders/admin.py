from django.contrib import admin
from .models import Order,OrderItem
from django.utils.translation import ugettext_lazy as _
from .forms import OrderUserForm


@admin.register(OrderItem)
class CartAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Cart info'), {'fields': ('user', 'item', 'quantity')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('item', 'user', 'quantity', 'price', 'total_amount','ordered')
    list_filter = ('item__price', 'user')
    search_fields = ('item', 'user')
    readonly_fields = ('created_at', 'modified_at',)


@admin.register(Order)
class CartProductMappingAdmin(admin.ModelAdmin):
    # form = OrderUserForm
    fieldsets = (
        (_('Order info'), {'fields': ('user', 'items')}),
        (_('Important dates'), {'fields': ('start_date', 'ordered_date')}),
    )
    list_display = ('user','ordered')
    list_filter = ('start_date', 'ordered_date',)
    search_fields = ('user',)
    readonly_fields = ('start_date', 'ordered_date',)

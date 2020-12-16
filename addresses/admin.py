from django.contrib import admin
from .models import Address
from django.utils.translation import ugettext_lazy as _
from import_export.admin import ImportExportModelAdmin
# from .forms import AddressForm


class AddressAdmin(admin.ModelAdmin):
    pass
    # form = AddressForm
    fieldsets = (
        (_('Bill Address info'), {'fields': ('user', 'name', 'phone_number', 'pincode', 'locality', 'address', 'city', 'landmark', 'address_type',)}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    # fields = ('user', 'name', 'phone_number', 'pincode', 'locality', 'address',
    #           'city', 'landmark', 'address_type',)
    list_display = ('user','name','phone_number','city','pincode',)
    readonly_fields = ('created_at', 'modified_at')
    radio_fields = {'address_type': admin.HORIZONTAL}


admin.site.register(Address, AddressAdmin)

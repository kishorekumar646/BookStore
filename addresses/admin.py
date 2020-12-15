from django.contrib import admin
from .models import Address
from import_export.admin import ImportExportModelAdmin
# from .forms import AddressForm


class AddressAdmin(admin.ModelAdmin):
    pass
    # form = AddressForm
    # fields = ('nick_name', 'address_contact_name', 'address_contact_number',
    #           'address_type', 'address_line1', 'state', 'city', 'pincode_link', 'area')
    
    # radio_fields = {'address_type': admin.HORIZONTAL}


admin.site.register(Address, AddressAdmin)

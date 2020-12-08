from django.contrib import admin
from .models import (Address, State, City, Pincode, Area)
from import_export.admin import ImportExportModelAdmin
from .forms import AddressForm


class PincodeAdmin(ImportExportModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    form = AddressForm
    fields = ('nick_name', 'address_contact_name', 'address_contact_number',
              'address_type', 'address_line1', 'state', 'city', 'pincode_link')
    raw_id_fields = ('state',)


admin.site.register(Area)
admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Pincode, PincodeAdmin)

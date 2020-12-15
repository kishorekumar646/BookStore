from django.contrib import admin
from .models import (Address, State, City, Pincode)
from import_export.admin import ImportExportModelAdmin
# from .forms import AddressForm


class PincodeAdmin(ImportExportModelAdmin):
    list_select_related = ('city',)
    list_display = ('pincode', 'city')
    # autocomplete_fields = ('city',)
    search_fields = ('city__city_name', 'pincode')


class CityAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass
    # form = AddressForm
    # fields = ('nick_name', 'address_contact_name', 'address_contact_number',
    #           'address_type', 'address_line1', 'state', 'city', 'pincode_link','area')
    # raw_id_fields = ('state',)
    # radio_fields = {'address_type': admin.HORIZONTAL}


admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Pincode, PincodeAdmin)

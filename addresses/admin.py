from django.contrib import admin
from .models import (Address, State, City, Pincode, Area)
from import_export.admin import ImportExportModelAdmin
from .forms import StateForm


class PincodeAdmin(ImportExportModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Area)
admin.site.register(State)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Pincode, PincodeAdmin)

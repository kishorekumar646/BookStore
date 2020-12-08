from django.contrib import admin
from .models import (Address,State,City,Pincode,Area)
from import_export.admin import ImportExportModelAdmin

class StateAdmin(admin.ModelAdmin):
    pass


class PincodeAdmin(ImportExportModelAdmin):
    pass


class CityAdmin(admin.ModelAdmin):
    pass


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Area)
admin.site.register(State, StateAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Pincode, PincodeAdmin)

from django import forms
from django.core.validators import RegexValidator
from .models import Address
from dal import autocomplete


class AddressForm(forms.ModelForm):
    '''
    Billing Address
    '''
    class Meta:
        model = Address
        fields = ['name', 'phone_number', 'pincode', 'locality',
                  'address', 'city', 'landmark', 'address_type']

    def save(self, commit=True):
        bill_address = super(AddressForm, self).save(commit=False)
        bill_address.name = self.cleaned_data.get('name')
        bill_address.phone_number = self.cleaned_data.get('phone_number')
        bill_address.pincode = self.cleaned_data.get('pincode')
        bill_address.locality = self.cleaned_data.get('locality')
        bill_address.address = self.cleaned_data.get('address')
        bill_address.city = self.cleaned_data.get('city')
        bill_address.landmark = self.cleaned_data.get('landmark')
        bill_address.address_type = self.cleaned_data.get('address_type')

        return bill_address


from django import forms
from django.core.validators import RegexValidator
from .models import (State, City, Pincode, Address, Area)
from dal import autocomplete


class AddressForm(forms.ModelForm):
    state = forms.ModelChoiceField(
        queryset=State.objects.all(),
        widget=autocomplete.ModelSelect2(url='state-autocomplete',),
        required=True
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=autocomplete.ModelSelect2(url='city_autocomplete',
                                         forward=('state',)),
        required=True
    )
    pincode_link = forms.ModelChoiceField(
        queryset=Pincode.objects.all(),
        widget=autocomplete.ModelSelect2(url='pincode_autocomplete',
                                         forward=('city',)),
        required=True
    )

    class Meta:
        model = Address
        fields = ('nick_name', 'address_contact_name',
                  'address_contact_number', 'address_type', 'address_line1',
                  'state', 'city', 'pincode_link')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nick_name'].required = True
        self.fields['address_contact_name'].required = True
        self.fields['address_contact_number'].required = True

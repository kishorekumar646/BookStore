from django import forms
from django.core.validators import RegexValidator
from .models import Address
from dal import autocomplete


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['name', 'phone_number', 'pincode', 'locality',
                  'address', 'city', 'landmark', 'address_type']

# class AddressForm1(forms.ModelForm):
#     state = forms.ModelChoiceField(
#         queryset=State.objects.all(),
#         widget=autocomplete.ModelSelect2(url='state-autocomplete',),
#         required=True
#     )
#     city = forms.ModelChoiceField(
#         queryset=City.objects.all(),
#         widget=autocomplete.ModelSelect2(url='city-autocomplete',
#                                          forward=('state',)),
#         required=True
#     )
#     pincode_link = forms.ModelChoiceField(
#         queryset=Pincode.objects.all(),
#         widget=autocomplete.ModelSelect2(url='pincode-autocomplete',
#                                          forward=('city',)),
#         required=True
#     )

#     class Meta:
#         model = Address
#         fields = ('address_contact_name',
#                   'address_contact_number', 'address_type', 'address_line1',
#                   'state', 'city', 'pincode_link','area')

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['address_contact_name'].required = True
#         self.fields['address_contact_number'].required = True
#         self.fields['area'].required = True

from django.contrib.auth import get_user_model
from dal import autocomplete
from django import forms
from .models import CartProductMapping


class OrderUserForm(forms.ModelForm):
    user = forms.ModelChoiceField(
        queryset=get_user_model().objects.all(),
        widget=autocomplete.ModelSelect2(
            url='order-user-autocomplete')
    )
    items = forms.ModelMultipleChoiceField(
        queryset=CartProductMapping.objects.all(),
        widget=autocomplete.ModelSelect2Multiple(
            url='item-user-autocomplete', forward=('user',)),

        required=True
    )

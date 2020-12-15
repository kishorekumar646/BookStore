from django.conf.urls import url
from django.urls import path
from .views import (StateAutocomplete, CityAutocomplete,
                    PinCodeAutocomplete, CheckoutView)

urlpatterns = [
    url(r'^state-autocomplete/$', StateAutocomplete.as_view(),
        name='state-autocomplete'),
    url(r'^city-autocomplete/$', CityAutocomplete.as_view(),
        name='city-autocomplete'),
    url(r'^pincode-autocomplete/$', PinCodeAutocomplete.as_view(),
        name='pincode-autocomplete'),
    path('checkout/', CheckoutView.as_view(), name='checkout')
]

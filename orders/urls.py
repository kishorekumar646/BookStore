from django.conf.urls import url, include
from django.urls import path
from .views import (add_to_cart, OrderUserAutocomplete,
                    ItemUserAutocomplete, remove_from_cart,
                    OrderSummaryView)

urlpatterns = [
    url(r'^order-user-autocomplete/$', OrderUserAutocomplete.as_view(),
        name='order-user-autocomplete'),
    url(r'^item-user-autocomplete/$', ItemUserAutocomplete.as_view(),
        name='item-user-autocomplete'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('oreder_summary/',OrderSummaryView.as_view(),name="oreder_summary"),
]

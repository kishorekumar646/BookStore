from django.conf.urls import url, include
from django.urls import path
from .views import add_to_cart, OrderUserAutocomplete, ItemUserAutocomplete

urlpatterns = [
    url(r'^order-user-autocomplete/$', OrderUserAutocomplete.as_view(),
        name='order-user-autocomplete'),
    url(r'^item-user-autocomplete/$', ItemUserAutocomplete.as_view(),
        name='item-user-autocomplete'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart')
]

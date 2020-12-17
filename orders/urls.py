from django.conf.urls import url, include
from django.urls import path
from .views import (add_to_cart, OrderUserAutocomplete,
                    ItemUserAutocomplete, remove_from_cart, decrease_quantity,
                    increase_quantity, OrderSummaryView,MyOrders)

urlpatterns = [
    url(r'^order-user-autocomplete/$', OrderUserAutocomplete.as_view(),
        name='order-user-autocomplete'),
    url(r'^item-user-autocomplete/$', ItemUserAutocomplete.as_view(),
        name='item-user-autocomplete'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('order_summary/', OrderSummaryView.as_view(), name='order_summary'),
    path('decrease_quantity/<slug>/', decrease_quantity, name='decrease_quantity'),
    path('increase_quantity/<slug>/', increase_quantity, name='increase_quantity'),
    path('my_orders/',MyOrders.as_view(),name='my_orders'),
]

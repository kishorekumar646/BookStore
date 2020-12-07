from django.conf.urls import url, include
from .views import add_to_cart, OrderUserAutocomplete, ItemUserAutocomplete

urlpatterns = [
    url(r'^add_to_cart/(?P<item_id>[-\w]+)/$',
        add_to_cart, name='add_to_cart'),
    url(r'^order-user-autocomplete/$', OrderUserAutocomplete.as_view(),
        name='order-user-autocomplete'),
    url(r'^item-user-autocomplete/$', ItemUserAutocomplete.as_view(),
        name='item-user-autocomplete'),
]

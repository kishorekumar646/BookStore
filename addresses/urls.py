from django.conf.urls import url
from django.urls import path
from .views import CheckoutView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]

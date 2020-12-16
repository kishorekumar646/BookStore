from django.conf.urls import url
from django.urls import path
from .views import CheckoutView,SucessView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('success/',SucessView.as_view(),name='success'),
]

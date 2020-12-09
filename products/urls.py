from django.conf.urls import url, include
from .views import BookProductList, home

urlpatterns = [
    url('product-list/', BookProductList, name='product-list'),
    url('home/', home, name='home'),
]

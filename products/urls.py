from django.conf.urls import url, include
from .views import BookProductList

urlpatterns = [
    url('product-list/', BookProductList, name='product-list'),
]

from django.conf.urls import url, include
from .views import BookProduct, home

urlpatterns = [
    url('home/', home, name='home'),
    url('product/', BookProduct, name='product')
]

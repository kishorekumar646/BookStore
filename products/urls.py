from django.conf.urls import url, include
from .views import BookProduct, HomeView

urlpatterns = [
    url('home/', HomeView.as_view(), name='home'),
    url(r'^product/(?P<slug>[\w-]+)/$', BookProduct, name='product')
]

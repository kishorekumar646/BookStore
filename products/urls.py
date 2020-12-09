from django.conf.urls import url, include
from django.urls import path
from .views import HomeView,BookDetailView

urlpatterns = [
    url('home/', HomeView.as_view(), name='home'),
    path('product/<slug>/', BookDetailView.as_view(), name='product')
]

from django.conf.urls import url, include
from django.urls import path
from .views import Login,Register,Logout

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
]

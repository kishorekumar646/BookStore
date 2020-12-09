from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookProductListSerializer


class HomeView(ListView):
    model = Book
    template_name = "home.html"

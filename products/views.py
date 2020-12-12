from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView,DetailView
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Book

class HomeView(ListView):
    model = Book
    paginate_by = 8
    template_name = "home.html"

class BookDetailView(DetailView):
    model = Book
    template_name = "product.html"

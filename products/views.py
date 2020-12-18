from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
# from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Book


class HomeView(ListView):

    '''   Display all products in home page      '''

    model = Book
    paginate_by = 8
    template_name = "home.html"


class BookDetailView(DetailView):

    '''   Get details of book by book name or author name      '''
    
    model = Book
    template_name = "product.html"

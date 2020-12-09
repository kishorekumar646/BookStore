from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookProductListSerializer


def BookProductList(request):
    product_list = Book.objects.all()

    context = {
        'product_list': product_list,
    }

    return render(request,'products/products_list.html', context)


def home(request):
    product_list = Book.objects.all()

    context = {
        'items': product_list,
    }

    return render(request,'home-page.html', context)
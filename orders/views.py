from django.shortcuts import render,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404
from products.models import Book
from .models import Cart

User = get_user_model()

@login_required()
def add_to_cart(request,**kwargs):
    product = Book.objects.filter(id=kwargs.get('item_id',"")).first()
    print(product)
    return HttpResponse("Successfull added to cart")

from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404
from products.models import Book
from dal import autocomplete
from .models import Cart, CartProductMapping

User = get_user_model()


class OrderUserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()
        if self.q:
            qs = qs.filter(first_name__icontains=self.q)
        return qs


class ItemUserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, *args, **kwargs):
        qs = Cart.objects.all()
        user_id = self.forwarded.get('user', None)
        if user_id:
            user = User.objects.get(id=user_id)
            qs = qs.filter(user=user)
        else:
            return qs.none()
        return qs


@login_required()
def add_to_cart(request, **kwargs):
    product = Book.objects.filter(id=kwargs.get('item_id', "")).first()
    print(product)
    return HttpResponse("Successfull added to cart")

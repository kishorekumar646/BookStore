from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from products.models import Book
from dal import autocomplete
from django.utils import timezone
from django.contrib import messages
from .models import Order, OrderItem

User = get_user_model()


class OrderUserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = User.objects.all()
        if self.q:
            qs = qs.filter(first_name__icontains=self.q)
        return qs


class ItemUserAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, *args, **kwargs):
        qs = OrderItem.objects.all()
        user_id = self.forwarded.get('user', None)
        if user_id:
            user = User.objects.get(id=user_id)
            qs = qs.filter(user=user)
        else:
            return qs.none()
        return qs


# @login_required()
def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(
        user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
            return redirect("product", slug=slug)

        else:
            messages.info(request, "This item was added to your cart")
            order.items.add(order_item)
            return redirect("product", slug=slug)

    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart")
    return redirect("product", slug=slug)


def remove_from_cart(request, slug):

    item = get_object_or_404(Book, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    if order_qs.exists():
        order = order_qs[0]

        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "The item was removed to your cart")
            return redirect("oreder_summary")

        else:
            messages.info(request, "The item was not in your cart")
            return redirect("oreder_summary")

    else:
        messages.info(request, "You don't have an active order")
        return redirect("oreder_summary")

    return redirect("oreder_summary")


class OrderSummaryView(View):

    def get(self,*args,**kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request,'cart.html',context)

        except ObjectDoesNotExist:
            messages.info(self.request,"You do not have an active order")
            return redirect(self.request,'oreder_summary')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from dal import autocomplete
from orders.models import Order, OrderItem
from .models import Address
from .forms import AddressForm


class CheckoutView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        try:
            form = AddressForm()
            order_item = OrderItem.objects.filter(
                user=self.request.user, ordered=False)
            print(order_item)
            if order_item.exists():
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                context = {
                    'form': form,
                    'object': order,
                }

                return render(self.request, 'checkout.html', context)

            else:
                raise ObjectDoesNotExist

        except ObjectDoesNotExist:
            messages.info(self.request, 'You don\'t have an active order')
            return render(self.request, 'cart.html')


class SucessView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):

        return render(self.request,'success.html',{})
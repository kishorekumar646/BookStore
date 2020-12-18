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
    '''
    Checkout Form
    '''

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

    def post(self, *args, **kwargs):

        form = AddressForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            print(form.errors)
            if form.is_valid():
                print("Form is valid")
                print(self.request.POST)
                bill_address = form.save()
                bill_address.user = self.request.user
                bill_address.save()
                order.billing_address = bill_address
                order.ordered = True
                order.save()
                return redirect('success')

            else:
                messages.info(self.request, '%s' % form.errors)
                return redirect('checkout')

        except ObjectDoesNotExist:
            return redirect('order_summary')


class SucessView(LoginRequiredMixin, View):
    '''
    successfully order items details
    '''

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=True)
            for item in order.items.all():
                item.ordered = True
                item.save()
            context = {
                'object': order
            }
            return render(self.request, 'success.html', context)

        except ObjectDoesNotExist:
            return redirect('order_summary')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from dal import autocomplete
from orders.models import Order, OrderItem
from .models import State, City, Pincode
from .forms import AddressForm


class StateAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, *args, **kwargs):
        qs = State.objects.all()
        if self.q:
            qs = qs.filter(state_name__icontains=self.q)
        return qs


class CityAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, *args, **kwargs):
        qs = City.objects.all()
        state_id = self.forwarded.get('state', None)
        if state_id:
            state = State.objects.get(id=state_id)
            qs = qs.filter(state=state).order_by('city_name')
        else:
            return qs.none()
        return qs


class PinCodeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self, *args, **kwargs):
        qs = Pincode.objects.all()
        city_id = self.forwarded.get('city', None)
        if city_id:
            city = City.objects.get(id=city_id)
            qs = qs.filter(city=city).order_by('pincode')
        else:
            return qs.none()
        return qs


class CheckoutView(LoginRequiredMixin, View):

    def get(self, *args, **kwargs):
        try:
            form = AddressForm()
            order_item = OrderItem.objects.filter(
                user=self.request.user, ordered=False)
            print(order_item)
            if order_item.exists():
                order = Order.objects.get(user=self.request.user, ordered=False)
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

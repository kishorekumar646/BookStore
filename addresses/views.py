from django.shortcuts import render
from dal import autocomplete
from .models import State, City, Pincode


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

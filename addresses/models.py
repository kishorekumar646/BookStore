from django.db import models
from bookstore_backend.validators import (
    AddressNameValidator, MobileNumberValidator, PinCodeValidator, NameValidator)
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    state_name = models.CharField(max_length=255, validators=[NameValidator])
    state_code = models.CharField(max_length=2, null=True,
                                  blank=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(
        State, related_name='state_city', null=True, blank=True, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=255, validators=[
                                 NameValidator], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.city_name


class Pincode(models.Model):
    city = models.ForeignKey(City, related_name='city_pincode',
                             on_delete=models.CASCADE)
    pincode = models.CharField(max_length=6, validators=[
                               PinCodeValidator], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
        unique_together = ['city', 'pincode']
        verbose_name_plural = _("Pincodes")

    def __str__(self):
        return self.pincode

class Area(models.Model):
    city = models.ForeignKey(City, related_name='city_area',
                             null=True, blank=True, on_delete=models.CASCADE)
    area_name = models.CharField(max_length=255, validators=[NameValidator])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.area_name


class Address(models.Model):
    nick_name = models.CharField(max_length=255, null=True, blank=True)
    address_line1 = models.CharField(
        max_length=255, validators=[AddressNameValidator])
    address_contact_name = models.CharField(
        max_length=255, null=True, blank=True)
    address_contact_number = models.CharField(
        validators=[MobileNumberValidator], max_length=10, blank=True)
    pincode = models.CharField(
        validators=[PinCodeValidator], max_length=6, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "%s - %s" % (self.nick_name, self.address_line1)

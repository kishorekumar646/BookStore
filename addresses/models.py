from django.db import models
from bookstore_backend.validators import (
    AddressNameValidator, MobileNumberValidator, PinCodeValidator, NameValidator)
from django.utils.translation import ugettext_lazy as _

ADRESS_TYPE_CHOICE = (
    ("home", "Home"),
    ("office", "Office"),
    ("other", "Other"),
)


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
    pincode_link = models.ForeignKey(Pincode, related_name='pincode_address',
                                     null=True, blank=True,
                                     on_delete=models.DO_NOTHING)

    state = models.ForeignKey(State, related_name='state_address',
                              on_delete=models.CASCADE, blank=True, null=True)
    city = models.ForeignKey(
        City, related_name='city_address', on_delete=models.CASCADE)
    area = models.CharField(max_length=255, null=True, blank=True)
    address_type = models.CharField(
        max_length=255, choices=ADRESS_TYPE_CHOICE, default='home')
    latitude = models.FloatField(default=0, null=True, blank=True)
    longitude = models.FloatField(default=0, null=True, blank=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "%s - %s" % (self.nick_name, self.address_line1)

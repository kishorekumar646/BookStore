from django.db import models
from bookstore_backend.validators import (
    AddressNameValidator, MobileNumberValidator, PinCodeValidator, NameValidator)
from django.utils.translation import ugettext_lazy as _

ADRESS_TYPE_CHOICE = (
    ("home", "Home"),
    ("office", "Office"),
    ("other", "Other"),
)


class Address(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(
        validators=[MobileNumberValidator], max_length=10, blank=True)
    pincode = models.CharField(
        validators=[PinCodeValidator], max_length=6, blank=True)
    locality = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    landmark = models.CharField(max_length=50,null=True,blank=True)
    address_type = models.CharField(
        max_length=255, choices=ADRESS_TYPE_CHOICE, default='home')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.name)

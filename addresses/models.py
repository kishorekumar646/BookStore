from django.db import models
from django.contrib.auth import get_user_model
from bookstore_backend.validators import (
    AddressNameValidator, MobileNumberValidator, PinCodeValidator, NameValidator)
from django.utils.translation import ugettext_lazy as _

ADRESS_TYPE_CHOICE = (
    ("home", "Home"),
    ("office", "Office"),
    ("other", "Other"),
)


class Address(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=255,)
    phone_number = models.CharField(
        validators=[MobileNumberValidator], max_length=10)
    pincode = models.CharField(
        validators=[PinCodeValidator], max_length=6)
    locality = models.CharField(max_length=20,)
    address = models.CharField(max_length=50,)
    city = models.CharField(max_length=50,)
    landmark = models.CharField(max_length=50,)
    address_type = models.CharField(
        max_length=255, choices=ADRESS_TYPE_CHOICE, default='home')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return "%s" % (self.user.first_name)

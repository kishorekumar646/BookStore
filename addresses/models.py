from django.db import models
from bookstore_backend.validators import (
    AddressNameValidator, MobileNumberValidator, PinCodeValidator)


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

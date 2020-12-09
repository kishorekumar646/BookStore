from django.db import models
from django.contrib.auth import get_user_model
from products.models import Book
from addresses.models import Address

ORDER_STATUS = (
    ("ordered_to_brand", "Ordered To Brand"),
    ("partially_delivered", "Partially Delivered"),
    ("delivered", "Delivered"),
)


class Cart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    product = models.OneToOneField(
        Book, on_delete=models.SET_NULL, null=True, blank=True)
    qty = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title

    @property
    def price(self):
        return (self.product.price)

    @property
    def total_amount(self):
        return (self.qty * self.product.price)

    class Meta:
        ordering = ['-id']
        verbose_name = "Cart"


class CartProductMapping(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField('Cart', related_name='cart_order')

    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    class Meta:
        verbose_name = "Place Order"

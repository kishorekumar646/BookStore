from django.db import models
from django.contrib.auth import get_user_model
from products.models import Book
from addresses.models import Address
import decimal

ORDER_STATUS = (
    ("ordered_to_brand", "Ordered To Brand"),
    ("partially_delivered", "Partially Delivered"),
    ("delivered", "Delivered"),
)


class OrderItem(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    item = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.item.title

    @property
    def price(self):
        return (self.item.price)

    @property
    def total_amount(self):
        return (self.quantity * self.item.price)

    class Meta:
        ordering = ['-id']
        verbose_name = "Cart"


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem', related_name='cart_order')

    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.first_name

    def get_total_amount(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.total_amount

        return total

    class Meta:
        verbose_name = "Place Order"

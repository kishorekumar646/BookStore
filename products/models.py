from django.db import models
from bookstore_backend.validators import *

CATEGORY = (
    (1, "Programming"),
    (2, "Networking"),
    (3, "Python")
)


class Book(models.Model):
    title = models.CharField(
        max_length=255, validators=[BookNameValidator],)
    author = models.CharField(
        max_length=255, validators=[BookAuthorValidator],)
    image_cover = models.ImageField(
        upload_to='upload_photos/book_photos/', null=True, blank=True)
    description = models.CharField(max_length=255, validators=[
                                        BookNameValidator], null=True, blank=True)
    category = models.PositiveSmallIntegerField(
        choices=CATEGORY, default=None, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s - %s' % (self.title, self.author)

    class Meta:
        verbose_name = 'Book product'

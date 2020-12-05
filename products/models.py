from django.db import models
from bookstore_backend.validators import *

CATEGORY = (
    (1, "Programming"),
    (2, "Networking"),
    (3, "Python")
)


class Book(models.Model):
    book_title = models.CharField(
        max_length=255, validators=[BookNameValidator],)
    book_author = models.CharField(
        max_length=255, validators=[BookAuthorValidator],)
    book_description = models.CharField(max_length=255, validators=[
                                        BookNameValidator], null=True, blank=True)
    book_category = models.PositiveSmallIntegerField(
        choices=CATEGORY, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return '%s - %s' % (self.book_title, self.book_author)

    class Meta:
        verbose_name = 'Book product'

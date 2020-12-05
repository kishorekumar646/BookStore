from django.db import models


class Book(models.Model):
    book_title = models.CharField(max_length = 150)
    

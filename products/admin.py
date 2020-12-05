from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Book info'), {'fields': (
            ('book_title', 'book_author'), 'book_description', 'book_category')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('book_title','book_author','created_at')
    list_filter = ('created_at', 'modified_at')
    search_fields = ('book_title','book_author')
    readonly_fields = ('created_at', 'modified_at',)
    list_per_page = 10

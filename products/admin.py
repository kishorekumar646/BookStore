from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Book info'), {'fields': (
            ('title', 'author'), 'description', 'category')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('title','author','created_at')
    list_filter = ('created_at', 'modified_at')
    search_fields = ('book_title','book_author')
    readonly_fields = ('created_at', 'modified_at',)
    list_per_page = 10

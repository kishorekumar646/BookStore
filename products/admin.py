from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Book info'), {'fields': (('title', 'author'), 'description', 'category',
                                    ('image_cover','book_photo_thumbnail'),'price')}),
        (_('Important dates'), {'fields': ('created_at', 'modified_at')}),
    )
    list_display = ('title','author','price','created_at')
    list_filter = ('price','created_at', 'modified_at')
    search_fields = ('book_title','book_author')
    radio_fields = {'category': admin.HORIZONTAL}
    readonly_fields = ('created_at', 'modified_at','book_photo_thumbnail',)
    list_per_page = 10

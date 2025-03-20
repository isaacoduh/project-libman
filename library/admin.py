from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin panel for book management"""
    list_display = ('title', 'author', 'isbn', 'page_count', 'available')
    search_fields = ('title', 'author','isbn')
    list_filter = ('available',)
    ordering = ('title',)
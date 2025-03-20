from django.contrib import admin
from .models import Book, Loan


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin panel for book management"""
    list_display = ('title', 'author', 'isbn', 'page_count', 'available')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('available',)
    ordering = ('title',)


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    """Admin panel for loans management"""
    list_display = ('user', 'book', 'borrowed_at', 'returned_at')
    list_filter = ('returned_at',)
    search_fields = ('user__email', 'book__title')
    ordering = ('-borrowed_at',)

    def get_readonly_fields(self, request, obj=None):
        """Make fields readonly after creation"""
        if obj:
            return ['user', 'book', 'borrowed_at']
        return []

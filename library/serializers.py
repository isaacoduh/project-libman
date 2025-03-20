from rest_framework import serializers
from .models import Book, Loan
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """Serializers for books"""

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'page_count', 'available']

from rest_framework import generics, permissions, status
from rest_framework.response import  Response
from rest_framework.pagination import PageNumberPagination

from .models import Book
from .serializers import BookSerializer

class BookPagination(PageNumberPagination):
    """Pagination for list of books"""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50


class BookListView(generics.ListAPIView):
    """Public API to list all books (paginated)"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = BookPagination
    permission_classes = [permissions.AllowAny]

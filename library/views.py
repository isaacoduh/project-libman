from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer


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


class LoanListView(generics.ListAPIView):
    """API for users to view their loans."""
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Return only loans of the logged in users"""
        return Loan.objects.filter(user=self.request.user).order_by('-borrowed_at')


class BorrowBookView(generics.CreateAPIView):
    """API to borrow a book (users only)"""
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]


class ReturnBookView(generics.UpdateAPIView):
    """API to return a borrowed book"""
    serializer_class = LoanSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Only allow retuning books that the user borrowed"""
        return Loan.objects.filter(user=self.request.user, returned_at__isnull=True)

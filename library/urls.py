from django.urls import path
from .views import BookListView, LoanListView, BorrowBookView, ReturnBookView

urlpatterns = [
    path('books/', BookListView.as_view(), name="book-list"),

    path('loans/', LoanListView.as_view(), name="loan-list"),
    path('borrow/', BorrowBookView.as_view(), name="borrow-book"),
    path('return/<int:pk>', ReturnBookView.as_view(), name="return-book")
]
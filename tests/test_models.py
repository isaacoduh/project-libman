import pytest
from library.models import Book, Loan
from django.contrib.auth import get_user_model


User = get_user_model()
@pytest.mark.django_db
def test_create_book():
    """Test creating a book instance."""
    book = Book.objects.create(
        title="The Pragmatic Programmer",
        author="Andrew Hunt, David Thomas",
        isbn="9780135957059",
        page_count=352,
        available=True
    )
    assert book.title == "The Pragmatic Programmer"
    assert book.available is True
    assert book.isbn == "9780135957059"


@pytest.mark.django_db
def test_create_loan():
    """Test creating a loan model."""
    user = User.objects.create_user(email="testuser@example.com", password="password123")
    book = Book.objects.create(title="1984", author="George Orwell", isbn="9780451524935", page_count=180,available=True)

    loan = Loan.objects.create(user=user, book=book)

    assert loan.user == user
    assert loan.book == book
    assert loan.borrowed_at is not None
    assert loan.returned_at is None


@pytest.mark.django_db
def test_return_book():
    """Test returning a borrowed book."""
    user = User.objects.create_user(email="testuser@example.com", password="password123")
    book = Book.objects.create(title="Django for Beginners", author="William S. Vincent", page_count=180, available=True)

    # Borrow book (manually set available=False)
    loan = Loan.objects.create(user=user, book=book)
    book.available = False
    book.save()

    book.refresh_from_db()
    assert book.available is False  # Book is unavailable when borrowed

    # Return book using model method
    loan.return_book()

    book.refresh_from_db()
    assert book.available is True
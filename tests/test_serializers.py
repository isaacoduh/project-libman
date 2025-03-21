import pytest
from library.models import Book, Loan
from library.serializers import BookSerializer, LoanSerializer
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIRequestFactory

User = get_user_model()

@pytest.mark.django_db
def test_book_serializer():
    """Test BookSerializer serialization and deserialization."""
    book = Book.objects.create(title="Clean Code", author="Robert C. Martin", isbn="9780132350884", page_count=345, available=True)

    serializer = BookSerializer(book)
    assert serializer.data["title"] == "Clean Code"
    assert serializer.data["available"] is True

@pytest.mark.django_db
def test_loan_serializer():
    """Test LoanSerializer handling loan creation and return logic."""
    user = User.objects.create_user(email="test@example.com", password="password")
    book = Book.objects.create(title="Python Crash Course", page_count=345, author="Eric Matthes", available=True)

    loan_data = {"book_id": book.id}

    # Simulate request object with authenticated user
    factory = APIRequestFactory()
    request = factory.post("/fake-url/", data=loan_data)
    request.user = user

    # Borrow book
    serializer = LoanSerializer(data=loan_data, context={"request": request})
    assert serializer.is_valid(), serializer.errors
    loan = serializer.save()

    book.refresh_from_db()
    assert book.available is False

    # Return book
    return_serializer = LoanSerializer(instance=loan, data={"returned_at": timezone.now()}, partial=True)
    assert return_serializer.is_valid(), return_serializer.errors
    return_serializer.save()

    book.refresh_from_db()
    assert book.available is True


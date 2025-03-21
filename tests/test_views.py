import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from library.models import Book, Loan

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def create_user():
    return User.objects.create_user(email="user@example.com", password="password")


@pytest.fixture
def create_admin():
    return User.objects.create_user(email="admin@example.com", password="adminpassword")


@pytest.fixture
def create_book():
    return Book.objects.create(title="Django Unleashed", author="Andrew Pinkham", page_count=346, available=True)

@pytest.mark.django_db
def test_get_books(api_client, create_book):
    response = api_client.get('/api/library/books/')
    assert response.status_code == 200
    assert response.data['results'][0]['title'] == 'Django Unleashed'


@pytest.mark.django_db
def test_user_borrow_book(api_client, create_user, create_book):
    """Test borrowing a book as a logged-in user via API endpoint."""
    api_client.force_authenticate(user=create_user)

    response = api_client.post("/api/library/borrow/", {"book_id": create_book.id}, format="json")

    assert response.status_code == 201

    create_book.refresh_from_db()
    assert create_book.available is False


@pytest.mark.django_db
def test_user_return_book(api_client, create_user, create_book):
    """Test returning a borrowed book as a logged-in user."""
    api_client.force_authenticate(user=create_user)

    # Borrow the book first (persist loan in DB)
    loan = Loan.objects.create(user=create_user, book=create_book)

    # Ensure book is marked unavailable
    create_book.available = False
    create_book.save()

    # Ensure loan exists in DB before making request
    assert Loan.objects.filter(id=loan.id).exists(), "Loan was not created in the test database"

    # Make return request
    response = api_client.put(
        f"/api/library/return/{loan.id}",
        {},
        format="json"
    )

    assert response.status_code == 200
    create_book.refresh_from_db()
    assert create_book.available is True
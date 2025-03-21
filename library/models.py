from django.db import models
from users.models import User
from django.utils import timezone

# Create your models here.
class Book(models.Model):
    """Model representing a book in the library"""
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    page_count = models.PositiveIntegerField()
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return f"{self.title} by {self.author}"


class Loan(models.Model):
    """Model representing the borrowing of a book"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="loans")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="loans")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def return_book(self):
        """Mark book as returned"""
        self.returned_at = timezone.now()
        self.book.available = True
        self.book.save()
        self.save()

    def __str__(self):
        return f"{self.user.email} borrowed {self.book.title}"
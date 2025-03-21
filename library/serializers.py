from rest_framework import serializers
from .models import Book, Loan
from django.utils import timezone


class BookSerializer(serializers.ModelSerializer):
    """Serializers for books"""

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'isbn', 'page_count', 'available']


class LoanSerializer(serializers.ModelSerializer):
    """Serializer for loans"""
    book = BookSerializer(read_only=True)
    book_id = serializers.IntegerField(write_only=True) # accepts a book Id to borrow

    class Meta:
        model = Loan
        fields = ['id', 'book','book_id','borrowed_at','returned_at']

    def create(self, validated_data):
        """Handles borrowing a book"""

        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            raise serializers.ValidationError("User must be authenticated to borrow a book.")
        user = request.user
        book_id = validated_data.pop('book_id')

        # check if book exists
        try:
            book = Book.objects.get(id=book_id, available=True)
        except Book.DoesNotExist:
            raise serializers.ValidationError('Book is not available')

        # create a loan request
        loan = Loan.objects.create(user=user, book=book, **validated_data)

        # mark book as unavailable
        book.available = False
        book.save(update_fields=['available'])

        return loan

    def update(self, instance, validated_data):
        """Handle returning a book"""
        if instance.returned_at:
            raise serializers.ValidationError('This book already been returned!')
        instance.returned_at = timezone.now()

        # set book availability
        book = instance.book
        book.available = True
        book.save(update_fields=['available'])

        instance.save()
        return instance


class ReturnBookSerializer(serializers.ModelSerializer):
    """Serializer for returning a borrowed book"""

    class Meta:
        model = Loan
        fields = ["returned_at"]

    def update(self, instance, validated_data):
        """Handle returning a book"""
        if instance.returned_at:
            raise serializers.ValidationError('This book has already been returned!')

        instance.returned_at = timezone.now()

        # Mark the book as available again
        book = instance.book
        book.available = True
        book.save(update_fields=['available'])

        instance.save()
        return instance
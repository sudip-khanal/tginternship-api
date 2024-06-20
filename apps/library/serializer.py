
from rest_framework import serializers
from apps.book.models import Book
from apps.library.models import Library
from apps.user.models import User
from apps.user.serializer import UserSerializer
from apps.book.serializer import BookSerializer


class LibrarySerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)
    # owner = UserSerializer(sorce='user')
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


    class Meta:
        model = Library
        fields = ['id','name', 'address', 'books', 'owner']


    def create(self, validated_data):
        books = validated_data.pop('books')
        library=Library.objects.create(**validated_data)
        for book_data in books:
            book,created = Book.objects.get_or_create(**book_data)
            library.books.add(book)
        return library

    def update(self, instance, validated_data):
        books = validated_data.pop('books')
        instance = super().update(instance, validated_data)

        # Clear current books
        instance.books.clear()

        for book_data in books:
            book, created = Library.objects.get_or_create(**book_data)
            instance.books.add(book)

        return instance


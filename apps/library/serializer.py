# apps/book/serializers.py

from rest_framework import serializers
from apps.library.models import Library
from apps.user.serializer import UserSerializer
from apps.book.serializer import BookSerializer

class LibrarySerializer(serializers.ModelSerializer):
    owner = UserSerializer()  
    books = BookSerializer(many=True)  

    class Meta:
        model = Library
        fields = ['id', 'name', 'owner', 'address', 'books']

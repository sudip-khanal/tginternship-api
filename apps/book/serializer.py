from rest_framework import serializers
from apps.user.models import User
from apps.user.serializer import UserSerializer 
from apps.book.models import Book

class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    #owner = UserSerializer(source='owner')
    #owner = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())


    def create(self, validated_data):
        return Book.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.author = validated_data.get('author', instance.author)
        instance.owner_id = validated_data.get('owner', instance.owner_id)
        instance.save()
        return instance

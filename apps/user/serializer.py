from rest_framework import serializers
from apps.user.models import User

class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    first_name = serializers.CharField(max_length=30)
    last_name = serializers.CharField(max_length=30)
    address = serializers.CharField()
    gender = serializers.CharField()


    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.address= validated_data.get('address',instance.address)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.save()
        return instance

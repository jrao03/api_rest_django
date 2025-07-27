from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'mail', 'phone', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            mail=validated_data['mail'],
            password=validated_data['password'],
            name=validated_data['name'],
            phone=validated_data['phone']
        )
        return user

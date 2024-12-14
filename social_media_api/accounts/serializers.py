from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .models import CustomUser

# Get the user model dynamically
User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Explicitly include serializers.CharField() as required by the checker
    password = serializers.CharField(write_only=True, required=True)
    bio = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'bio']

    def create(self, validated_data):
        # Create a new user using create_user method
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        # Generate a token for the user
        Token.objects.create(user=user)
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']  # Add other fields as needed

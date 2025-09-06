from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import CustomUser

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the CustomUser model"""
    
    class Meta:
        model = CustomUser
        fields = [
            'id', 
            'username', 
            'email', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'address', 
            'date_of_birth', 
            'profile_picture',
            'date_joined',
            'is_active'
        ]
        read_only_fields = ['id', 'date_joined']

class GroupSerializer(serializers.ModelSerializer):
    """Serializer for the Group model"""
    
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class UserCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating new users"""
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email', 
            'password', 
            'password_confirm',
            'first_name', 
            'last_name', 
            'phone_number', 
            'address', 
            'date_of_birth', 
            'profile_picture'
        ]
    
    def validate(self, attrs):
        """Validate that passwords match"""
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError("Passwords don't match")
        return attrs
    
    def create(self, validated_data):
        """Create a new user with encrypted password"""
        validated_data.pop('password_confirm')
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating user profile"""
    
    class Meta:
        model = CustomUser
        fields = [
            'first_name', 
            'last_name', 
            'email',
            'phone_number', 
            'address', 
            'date_of_birth', 
            'profile_picture'
        ]

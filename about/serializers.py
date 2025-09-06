from rest_framework import serializers
from .models import AboutPage

class AboutPageSerializer(serializers.ModelSerializer):
    """Serializer for the AboutPage model"""
    
    class Meta:
        model = AboutPage
        fields = [
            'id',
            'title',
            'content',
            'mission',
            'vision',
            'created_at',
            'updated_at',
            'is_active'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

class AboutPageCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating about pages"""
    
    class Meta:
        model = AboutPage
        fields = [
            'title',
            'content',
            'mission',
            'vision',
            'is_active'
        ]

class AboutPageUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating about pages"""
    
    class Meta:
        model = AboutPage
        fields = [
            'title',
            'content',
            'mission',
            'vision',
            'is_active'
        ]

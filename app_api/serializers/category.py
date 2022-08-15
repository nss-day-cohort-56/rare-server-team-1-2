from rest_framework import serializers, status

from ..models.category import Category
class CategorySerializer(serializers.ModelSerializer):
    """JSON serializer for Category"""
    class Meta:
        model = Category
        fields = ('id', 'label')

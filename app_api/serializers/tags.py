from dataclasses import field
from rest_framework import serializers, status

from ..models.tag import Tag
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'label')
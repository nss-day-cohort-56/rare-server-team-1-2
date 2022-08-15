from rest_framework import serializers, status

from .rare_user import RareUserSerializer

from .category import CategorySerializer

from ..models.post import Post
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = RareUserSerializer()
    class Meta:
        model = Post
        fields = ('category', 'user', 'title', 'image_url', 'content', 'publication_date',)
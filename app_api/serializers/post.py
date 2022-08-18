from rest_framework import serializers, status

from .tags import TagSerializer

from .rare_user import RareUserSerializer

from .category import CategorySerializer

from ..models.post import Post
class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    user = RareUserSerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Post
        fields = ('id','category', 'user', 'title', 'image_url', 'content', 'publication_date', 'tags','approved')
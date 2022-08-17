from rest_framework import serializers, status

from .rare_user import RareUserSerializer

from ..models.comment import Comment
class CommentSerializer(serializers.ModelSerializer):
    author = RareUserSerializer()
    class Meta:
        model = Comment
        fields = ('id','content', 'author_id', 'created_on', 'author', 'post_id', 'subject')
        depth = 1
from xml.dom.minidom import Comment
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Comment
from ..serializers.comment import CommentSerializer
class CommentView(ViewSet):
    """Rare app comment view"""

    def list(self, request):
        """Handles GET requests for all comments"""

        post = request.query_params.get('post', None)
        comments = Comment.objects.all()
        if post is not None:
            comments = comments.filter(post_id=post)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations for comments"""

        
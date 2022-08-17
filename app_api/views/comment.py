from xml.dom.minidom import Comment
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Comment, comment
from app_api.models import Post
from ..models.rare_user import RareUser
from ..serializers.comment import CommentSerializer
class CommentView(ViewSet):
    """Rare app comment view"""

    def list(self, request):
        """Handles GET requests for all comments"""

        post = request.query_params.get('post', None)
        comments = Comment.objects.all().order_by("-created_on")
        if post is not None:
            comments = comments.filter(post_id=post)

        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        """Handles GET request for single comment"""
        comment = Comment.objects.get(pk=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def create(self, request):
        """Handles POST operations for comments"""

        author = RareUser.objects.get(user=request.auth.user)
        post = Post.objects.get(pk=request.data["post_id"])
        
        comment = Comment.objects.create(
            content=request.data["content"],
            author=author,
            post=post
        )
        serializer = CommentSerializer(comment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handle PUT requests for a comment"""
        comment = Comment.objects.get(pk=pk)
        comment.content = request.data['content']
        comment.created_on = request.data['created_on']
        author = RareUser.objects.get(user=request.auth.user)
        comment.author = author
        post = Post.objects.get(pk=request.data["post_id"])
        comment.post = post
        comment.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk):
        """"Handles DELETE requests for a comment"""
        comment = Comment.objects.get(pk=pk)
        comment.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
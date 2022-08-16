from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action

from ..models.tag import Tag

from ..models.rare_user import RareUser

from ..models.category import Category

from ..serializers.post import PostSerializer

from ..models.post import Post
class PostView(ViewSet):
    def list(self, request):
        """ handle get all post.approved = true 
        """
        # need  
    
        posts = Post.objects.filter(approved=True, publication_date__lt = datetime.now() )
        search_term = request.query_params.get('search_term', None)
        if search_term is not None :
            post = post.filter(address__contains = search_term)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    def retrieve(self, request, pk):
        """Handle GET requests for single post

        Returns:
            Response -- JSON serialized game type
        """
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    def create(self, request):
        """HANDLE POST NEW post"""
        category = Category.objects.get(pk=request.data["category_id"])
        # user = RareUser.objects.get(pk=request.data['user_id'])
        user=request.auth.user
        rare_user = RareUser.objects.get(user__id = user.id)
        post = Post.objects.create(
        title = request.data['title'],  
        image_url = request.data['image_url'],
        content = request.data['content'],
        category = category,
        user = rare_user,
        publication_date = request.data['publication_date']
        )
        post.tags.add(*request.data['tags'])

        serializer = PostSerializer(post)
        return Response(serializer.data)
    def update(self, request, pk):
        """updates post"""
        category = Category.objects.get(pk=request.data["category_id"])

        post = Post.objects.get(pk=pk)
        post.title = request.data['title'],  
        post.image_url = request.data['image_url'],
        post.content = request.data['content'],
        post.publication_date = request.data['publication_date']
        post.category = category
        post.save()
        post.tags.clear()
        post.tags.add(*request.data['tags'])
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
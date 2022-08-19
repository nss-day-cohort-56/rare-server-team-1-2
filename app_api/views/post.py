from datetime import datetime
from turtle import title
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from rest_framework.decorators import action

from ..models.tag import Tag
from ..models import Subscription
from ..models.rare_user import RareUser

from ..models.category import Category

from ..serializers.post import PostSerializer

from ..models.post import Post
class PostView(ViewSet):
    def list(self, request):
        """ handle get all post.approved = true 
        """
        # need  
    
        posts = Post.objects.filter(approved=True, publication_date__lte = datetime.now() )
        search_term = request.query_params.get('search_term', None)
        tag_search = request.query_params.get('tag_search', None)
        if search_term is not None :
            posts = posts.filter(title__contains = search_term)
        if tag_search is not None:
            posts = posts.filter(tags__label__contains = tag_search)
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
        if user.is_staff == True :
            post = Post.objects.create(
            title = request.data['title'],  
            image_url = request.data['image_url'],
            content = request.data['content'],
            approved = True,
            category = category,
            user = rare_user,
            publication_date = request.data['publication_date']
            )
        else : 
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
        post.title = request.data["title"]  
        post.image_url = request.data['image_url']
        post.content = request.data['content']
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
    @action(methods= ['get'], detail=False)
    def my_posts(self, request):
        rare_user = RareUser.objects.get(user = request.auth.user)
        my_post = Post.objects.filter(user = rare_user)
        serializer = PostSerializer(my_post, many=True)
        return Response(serializer.data)
    @action(methods= ['get'], detail=False)
    def approve_post_list(self, request):
        post = Post.objects.filter(approved = False)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    @action(methods=['put'], detail=True)
    def approve_post(self,request,pk):
        post = Post.objects.get(pk=pk)
        post.approved = not post.approved
        post.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    @action(methods= ['get'], detail=False)
    def get_subscribed_posts(self, request):
        subscriptions = Subscription.objects.filter(follower__user = request.auth.user, ended_on = None)
        authors = []
        for subscription in subscriptions :
            authors.append(subscription.author)
        posts = Post.objects.filter(user__in = authors)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
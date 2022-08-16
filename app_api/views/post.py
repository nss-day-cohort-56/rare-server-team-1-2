from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action

from ..serializers.post import PostSerializer

from ..models.post import Post
class PostView(ViewSet):
    def list(self, request):
        """ handle get all work_orders.accepted = false 
        """
        # need  
        user=request.auth.user
        if user.is_staff == True: 
            posts = Post.objects.filter(approved=True, publication_date__lt = datetime.now() )
        search_term = request.query_params.get('search_term', None)
        if search_term is not None :
            post = post.filter(address__contains = search_term)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
from datetime import date
from ..models.rare_user import RareUser
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Subscription, subscription
from app_api.models import Post
from ..serializers.subscription import SubscriptionSerializer
class SubscriptionView(ViewSet):
    """Rare app subscription view"""

    def list(self, request):
        """Handles GET requests for all subscriptions"""

        subscriptions = Subscription.objects.filter(ended_on = None)
        serializer = SubscriptionSerializer(subscriptions, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single subscription

        Returns:
        Response -- JSON serialized subscription
        """
        try:
            subscription = Subscription.objects.get(pk=pk)
            serializer = SubscriptionSerializer(subscription)
            return Response(serializer.data)
        except Subscription.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status = status.HTTP_404_NOT_FOUND)
    

    def create(self, request):
        """Handles POST operations for subscriptions"""
        author = RareUser.objects.get(pk=request.data["author"])
        follower = RareUser.objects.get(user=request.auth.user)
        subscription = Subscription.objects.create(
            follower=follower,
            author=author
        )
        serializer = SubscriptionSerializer(subscription)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    def update(self,request, pk):
        """method to handle editing subscriptions"""
        follower = RareUser.objects.get(user=request.auth.user)
        subscription = Subscription.objects.get(author_id=pk, follower = follower, ended_on = None)
        subscription.ended_on= date.today()
        subscription.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        """"Handles DELETE requests for a subscription"""
        subscription = Subscription.objects.get(pk=pk)
        subscription.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
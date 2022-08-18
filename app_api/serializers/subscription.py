from rest_framework import serializers, status

from .rare_user import RareUserSerializer

from ..models.subscription import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    author = RareUserSerializer()
    class Meta:
        model = Subscription
        fields = ('id','follower', 'author', 'created_on', 'ended_on')
        depth  = 1
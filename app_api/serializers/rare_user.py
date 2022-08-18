from django.db import models
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ..models.rare_user import RareUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'is_staff')
class RareUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = RareUser
        fields = ('id','user')



class UserDetailedSerializer(serializers.ModelSerializer):
    """serializer to get more detailed information for user profile"""
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email','is_staff','date_joined')


class RareUserDetailedSerializer(serializers.ModelSerializer):
    """serializer to get more detailed information for user profile"""
    user = UserDetailedSerializer()
    class Meta:
        model = RareUser
        fields = ('id','user','profile_image_url','bio')
from django.db import models
from rest_framework import serializers, status
from django.contrib.auth.models import User
from ..models.rare_user import RareUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
class RareUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = RareUser
        fields = ('id','user')
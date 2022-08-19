from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from app_api.serializers import RareUserSerializer
from app_api.serializers import RareUserDetailedSerializer

from app_api.models import RareUser
from django.contrib.auth.models import User

class RareUserView(ViewSet):
    """Viewset that handles user requests
    """

    def retrieve(self,request,pk):
        """method to handle returning details of a single user"""

        rare_user = RareUser.objects.get(pk = pk)
        serializer = RareUserDetailedSerializer(rare_user)
        return Response(serializer.data)

    def list(self, request):
        """method to handle returning all users in alphabetical order by username"""


        rare_users = RareUser.objects.all().order_by("user__username")
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)

    def update(self,request,pk): 
        """method to handle updating a users information"""
        rare_user = RareUser.objects.get(pk = pk)
        user = User.objects.get(pk=rare_user.user.id)

        user.first_name = request.data["first_name"]
        user.last_name = request.data["last_name"]
        user.username = request.data["username"]
        user.email = request.data["email"]
        user.is_staff = request.data["is_staff"]
        rare_user.bio = request.data["bio"]

        user.save()
        rare_user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)


    @action(methods = ['get'], detail=False)
    def active(self, request):

        """method to handle returning ONLY ACTIVE USERS"""
        user = RareUser.objects.get(user = request.auth.user)

        """method to handle returning a list of all ACTIVE users"""

        rare_users = RareUser.objects.all().order_by("user__username")
        rare_users = rare_users.filter(user__is_active = True)
        for rare_user in rare_users:
            rare_user.following = user
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)

    @action(methods = ['get'], detail=False)
    def inactive(self, request):
        """method to handle returning a list of all INACTIVE users"""

        rare_users = RareUser.objects.all().order_by("user__username")
        rare_users = rare_users.filter(user__is_active = False)
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)

    @action(methods = ['put'], detail=True)
    def active_status(self, request, pk):
        """method to handle toggling a user's "is_active" status between true and false."""

        rare_user = RareUser.objects.get(pk=pk)
        user = User.objects.get(pk=rare_user.user.id)
        user.is_active = not user.is_active
        user.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

        # to get the opposite of a boolean, say NOT(space)
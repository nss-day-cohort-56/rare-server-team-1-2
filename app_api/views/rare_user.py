from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status

from app_api.serializers import RareUserSerializer
from app_api.models import RareUser

class RareUserView(ViewSet):
    """Viewset that handles user requests


    """
    def list(self, request):
        """method to handle returning all users in alphabetical order by username"""


        rare_users = RareUser.objects.all().order_by("user__username")
        serializer = RareUserSerializer(rare_users, many=True)
        return Response(serializer.data)
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from app_api.models import Tag
from app_api.serializers import TagSerializer 


class TagView(ViewSet):
    """Viewset for handling tag http requests
    """
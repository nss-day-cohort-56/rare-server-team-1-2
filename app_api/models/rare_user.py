from django.db import models
from django.contrib.auth.models import User

class RareUser(models.Model):
    """
    data model for rare user

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image_url = models.TextField()
    created_on = models.DateField(auto_now_add= True)
    active = models.BooleanField()
    bio = models.TextField()


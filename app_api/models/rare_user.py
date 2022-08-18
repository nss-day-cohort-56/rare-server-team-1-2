from django.db import models
from django.contrib.auth.models import User

class RareUser(models.Model):
    """
    data model for rare user

    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image_url = models.TextField()
    created_on = models.DateField(auto_now_add= True)
    active = models.BooleanField(default=True)
    bio = models.TextField()

    @property
    def following(self):
        return self.__following


    @following.setter

    def following(self, value):
        """For each subscription, checking to see if the person making the request follows the author"""
        for subscription in self.author_subscriptions.all():
            if subscription.follower.id == value.id:
                self.__following = True
            else:
                self.__following = False

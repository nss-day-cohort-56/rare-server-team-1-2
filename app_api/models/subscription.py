from django.db import models

class Subscription(models.Model):
    """data model for a subscription

    """

    follower = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="follower_subscriptions")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="author_subscriptions")
    created_on = models.DateField(auto_now_add= True)
    ended_on = models.DateField(null=True)
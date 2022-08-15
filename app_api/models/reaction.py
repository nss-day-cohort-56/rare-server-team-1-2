from django.db import models

class Reaction(models.Model):

    """data model for a reaction_
    """

    label = models.CharField(max_length=55)
    image_url = models.TextField()
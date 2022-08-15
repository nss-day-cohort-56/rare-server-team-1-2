from django.db import models

class Tag(models.Model):
    """data model for a tag
    """

    label = models.CharField(max_length=55)
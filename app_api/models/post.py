from django.db import models

class Post(models.Model):
    """data model for post

    """

    user = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=55)
    publication_date = models.DateField(auto_now_add= True)
    image_url = models.TextField()
    content = models.TextField()
    approved = models.BooleanField(default= False)
    reactions = models.ManyToManyField("Reaction", related_name="posts")
    tags = models.ManyToManyField("Tag", related_name="posts")
    def __str__(self):
        return self.title
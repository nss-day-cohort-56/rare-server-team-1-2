from django.db import models

class Comment(models.Model):
    """Data model for a comment
    """

    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey("RareUser", on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_on = models.DateField(auto_now_add= True)

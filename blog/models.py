from django.db import models


class Blog(models.Model):
    """
    Create blog model with corresponding requirements
    """
    title = models.CharField(null=False, max_length=50)
    description = models.TextField(null=True)
    image = models.ImageField(null=True)


class Comment(models.Model):
    """
    Comment blog model with corresponding requirements
    """
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

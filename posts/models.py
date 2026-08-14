from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # User submits draft which is stored in database, but not visible yet
    # If moderation allows post, it becomes published
    is_published = models.BooleanField(default = False)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # User submits draft comment which is stored in database, but not visible yet
    # If moderation approves, it becomes visible
    is_approved = models.BooleanField(default=False)
    


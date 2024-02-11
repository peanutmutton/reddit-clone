from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Subreddit(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True, max_length=100)
    members = models.ManyToManyField(User)
    creation_date = models.DateTimeField(auto_now_add=True)
class Post(models.Model):
    title = models.CharField(max_length=30)

    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    body = models.TextField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)
class PostVote(models.Model):
    type = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
class CommentVote(models.Model):
    type = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField(blank=True, null=True)

class Vote(models.Model):
    pass

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()

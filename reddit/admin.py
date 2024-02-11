from django.contrib import admin

from .models import Post, Comment, Subreddit

admin.site.register(Subreddit)
admin.site.register(Post)


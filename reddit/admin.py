from django.contrib import admin

from .models import Post, Comment, Subreddit, PostVote

admin.site.register(Subreddit)
admin.site.register(Post)
admin.site.register(PostVote)


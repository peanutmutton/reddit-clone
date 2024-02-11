from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model

from .models import Subreddit, Post

User = get_user_model()
def home_view(request):
    return render(request, 'index.html',{})

def user_view(request, username):
    user = get_object_or_404(User.objects.all(), username=username)
    return render(request, 'user.html', {'user': user})

def subreddit_view(request, name):
    subreddit = get_object_or_404(Subreddit.objects.all(), name=name)
    return render(request, 'subreddit.html', {'subreddit': subreddit})

def post_view(request, name, title):
    subreddit = get_object_or_404(Subreddit.objects.all(), name=name)
    post = get_object_or_404(Post.objects.all(), title=title)
    return render(request, 'post.html', {'subreddit': subreddit, 'post': post})
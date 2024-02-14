from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .models import Subreddit, Post
from .forms import SubmitPostForm

User = get_user_model()
def home_view(request):
    return render(request, 'index.html',{})

def user_view(request, username):
    user = get_object_or_404(User.objects.all(), username=username)
    return render(request, 'user.html', {'user': user})

def subreddit_view(request, name):
    subreddit = get_object_or_404(Subreddit.objects.all(), name=name)
    post_list = subreddit.post_set.all()
    return render(request, 'subreddit.html', {'subreddit': subreddit, 'post_list': post_list})

def post_view(request, name, pk):
    subreddit = get_object_or_404(Subreddit.objects.all(), name=name)
    post = get_object_or_404(Post.objects.all(), pk=pk)
    return render(request, 'post.html', {'subreddit': subreddit, 'post': post})
@login_required
def submit_post_view(request):
    '''Submit a post. Only logged-in users. 404 if wrong sub name'''
    if request.method == "POST":
        form = SubmitPostForm(request.POST)
        if form.is_valid():
            subreddit_name = form.cleaned_data['subreddit']
            subreddit = get_object_or_404(Subreddit.objects.all(), name=subreddit_name)
            post = Post(
                title=form.cleaned_data['title'],
                subreddit=subreddit,
                body = form.cleaned_data['body'],
                author = request.user,
            )
            post.save()
            return HttpResponseRedirect('thanks/')
    else:
        form = SubmitPostForm()
    return render(request, 'submit_post.html', {'form': form})
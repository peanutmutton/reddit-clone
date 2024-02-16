from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Subreddit, Post, PostVote
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

    user_votes = PostVote.objects.filter(user=request.user)

    return render(request, 'subreddit.html', {'subreddit': subreddit, 'post_list': post_list, 'user_votes': user_votes})

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


# src:https://www.geeksforgeeks.org/handling-ajax-request-in-django/
def like_post(request, pk, vote_type):
    if vote_type == 'true':
        vote_type = True
    elif vote_type == 'false':
        vote_type = False
    if request.method == 'GET':
        likedpost = get_object_or_404(Post.objects.all(), id=pk)
        try:
            vote = PostVote.objects.get(post=likedpost,user=request.user)



            if (vote.type == True and vote_type == True) or vote.type == False and vote_type == False:
                vote.delete()
            elif vote.type == False and vote_type == True:
                vote.type = True
                vote.save()
            elif vote.type == True and vote_type == False:
                vote.type = False
                vote.save()
        except:
            if vote_type == True:
                m = PostVote(post=likedpost, user=request.user, type=True)
            elif vote_type == False:
                m = PostVote(post=likedpost, user=request.user, type=False)
            m.save()
        return redirect(reverse('subreddit', args = [likedpost.subreddit.name]))
    else:
        return HttpResponse("Request method is not GET")

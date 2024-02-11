from django.urls import path

from .views import home_view, user_view, subreddit_view, post_view

urlpatterns = [
    path('', home_view, name='home'),
    path('u/<str:username>/', user_view, name='user'),
    path('r/<str:name>/', subreddit_view, name='subreddit'),
    path('r/<str:name>/<str:title>/', post_view, name='post'),

]
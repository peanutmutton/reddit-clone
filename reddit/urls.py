from django.urls import path

from .views import home_view, user_view, subreddit_view, post_view, submit_post_view

urlpatterns = [
    path('', home_view, name='home'),
    path('submit/', submit_post_view, name='submit'),
    path('u/<str:username>/', user_view, name='user'),
    path('r/<str:name>/', subreddit_view, name='subreddit'),
    path('r/<str:name>/<uuid:pk>/', post_view, name='post'),

]
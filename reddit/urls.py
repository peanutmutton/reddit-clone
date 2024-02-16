from django.urls import path, re_path


from .views import home_view, user_view, subreddit_view, post_view, submit_post_view, like_post

urlpatterns = [
    path('', home_view, name='home'),
    path('submit/', submit_post_view, name='submit'),
    path('likepost/<uuid:pk>/<str:vote_type>/', like_post, name='likepost' ),
    path('u/<str:username>/', user_view, name='user'),
    path('r/<str:name>/', subreddit_view, name='subreddit'),
    path('r/<str:name>/<uuid:pk>/', post_view, name='post'),

]
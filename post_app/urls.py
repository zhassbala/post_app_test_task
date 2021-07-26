from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),                # index page
    path('register', views.register, name='register'),  # registers a user without logging in

    path('login', views.login, name='login'),           # log in a user, creates a token and responds with
                                                        # a cookie which contains that token

    path('logout', views.logout, name='logout'),        # destroys a token in browser cookies
    path('get_user', views.get_user, name='get_user'),  # responds with basic info about the logged user
    path('my_posts', views.get_posts, name='get_posts'),
    path('post_create', views.post_create, name='post_create'),
    path('post_update', views.post_update, name='post_update'),
    path('post_delete', views.post_delete, name='post_delete'),
    path('get_posts_by_tags', views.get_posts_by_tags, name='get_posts_by_tags'),
    path('get_posts_by_date', views.get_posts_by_date, name='get_posts_by_date'),
]

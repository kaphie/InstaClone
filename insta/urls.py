from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import (
    PostlistView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    saved_posts,
    PostLikeToggle,
    
)

app_name = 'insta'

urlpatterns = [
    #local : http://127.0.0.1:8000/

    path('', PostlistView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
    path('<int:id>', PostDetailView.as_view(), name='post_detail'),
    path('new/', PostCreateView.as_view(), name='post_new'),
    path('<int:id>/update/', PostUpdateView.as_view(), name='post_update'),
    path('<int:id>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:id>/likes/', PostLikeToggle.as_view(), name='like_toggle'),
    path('saved/', saved_posts, name='saved_posts'),
    # path('login/', auth_views.login, name='login'),
    # path('user_profile/', auth_views.user_profile, name='user_profile'),

]


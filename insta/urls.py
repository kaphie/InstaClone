from django.urls import path, include
from .views import (
    PostlistView,
    PostCreateView,
)

app_name = 'insta'

urlpatterns = [
    #local : http://127.0.0.1:8000/

    path('', PostlistView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name="post_create"),
]
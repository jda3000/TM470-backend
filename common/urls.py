from django.urls import path

from .api import *

urlpatterns = [
    # comments
    path('comment_list', CommentList.as_view()),
    path('comment_detail', CommentDetail.as_view()),
    # likes
    path('like_detail', LikeDetail.as_view()),
    path('like_list', ListList.as_view()),
]

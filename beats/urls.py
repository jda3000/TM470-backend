from django.urls import path

from beats.api import *

urlpatterns = [
    path('beat_public_list', BeatsPublicList.as_view()),
    path('beat_following_list', BeatsFollowingList.as_view()),
    path('beat_list_user', BeatsUserList.as_view()),
    path('beat_detail', BeatDetail.as_view(), name='beat_detail'),
    path('beat_map', BeatsPublicMap.as_view())
]

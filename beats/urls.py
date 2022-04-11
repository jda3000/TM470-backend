from django.urls import path

from beats.api import *

urlpatterns = [
    path('list', BeatsList.as_view()),
    path('beat_detail', BeatDetail.as_view(), name='beat_detail'),
]

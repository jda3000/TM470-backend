from django.urls import path

from beats.api.list import BeatsList
from beats.api.detail import BeatDetail

urlpatterns = [
    path('list', BeatsList.as_view()),
    path('beat_detail', BeatDetail.as_view()),
]

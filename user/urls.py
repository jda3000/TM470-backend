from django.urls import path

from .api import *

urlpatterns = [
    # comments
    path('current_user', CurrentUser.as_view()),
]

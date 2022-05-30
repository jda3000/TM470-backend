"""TM470_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views #import this

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .settings.jwt_token import CustomTokenObtainPairView

from user.api.forgotten_password import ForgottenPassword
from user.api.regsiter import Register

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # user
    path('user/api/', include(('user.urls', 'user'), namespace='users')),
    # sessions
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', Register.as_view(), name='register'),
    path('api/forgotten_password/', ForgottenPassword.as_view(), name='forgotten_password'),
    # apps
    path('beats/api/', include(('beats.urls', 'beats'), namespace='beats')),
    path('common/api/', include(('common.urls', 'common'), namespace='common')),
    # password reset default views
    path('accounts/', include('django.contrib.auth.urls'))
]


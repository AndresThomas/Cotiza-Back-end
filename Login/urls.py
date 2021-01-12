from django.contrib import admin
from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.urls import path, re_path

from Login.views import CustomAuthToken

urlpatterns = [
    
    re_path(r'^', CustomAuthToken.as_view()),

]

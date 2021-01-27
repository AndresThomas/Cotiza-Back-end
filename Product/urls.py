from django.urls import re_path
from Product import views

urlpatterns = [    
    re_path(r'^', views.Product.as_view()),
]
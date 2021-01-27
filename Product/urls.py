from django.urls import re_path
from Product import views

urlpatterns = [        
    re_path(r'details/(?P<id>\d+)/$', views.ProductDetail.as_view()),
    re_path(r'^', views.Product.as_view()),
]
from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from Product.serializer import Product, ProductSerializer
from .models import Product as P

# Create your views here.


class Product(ObtainAuthToken):

    def get(self, request, format=None):
        print("Get in products")
        queryset = P.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, format = None):
        print(request.data)
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            product = serializer.save()
            datas = serializer.data            
            return Response(datas, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    

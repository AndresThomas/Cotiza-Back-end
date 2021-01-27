from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from Product.serializer import Product, ProductSerializer
from .models import Product as P

# Create your views here.


class Product(APIView):

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
class ProductDetail(APIView):
    print("entrando a details")
    def get_object(self,id):
        try:
            return P.objects.get(pk = id)
        except P.DoesNotExist:
            return 404
    
    def get(self, request, id ,format = None):
        example_object = self.get_object(id) 
        if example_object != 404:
            serializer = ProductSerializer(example_object)
            return Response(serializer.data)
        return Response("No hay datos")
    
    def put(self,request,id,format = None):
        modify = self.get_object(id)

        if modify != 404:
            serializer = ProductSerializer(modify, data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas)
            else:
                return Response("Ingrese un formato valido")
        else:
            return Response("Este elemento no existe")

    def delete(self, request, id, format=None):
        product = self.get_object(id)
        if product != 404:
            product.delete()
            return Response('Elemento borrado', status=status.HTTP_200_OK)
        else:
            return Response(product, status=status.HTTP_404_NOT_FOUND)
    

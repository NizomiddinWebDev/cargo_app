from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import Client, Product, Mark
from .serializers import ClientSerializer, ProductSerializer, MarkSerializer, NewMarkSerializer, ClientNewSerializer


# Create your views here.


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProductListDestroy(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset.delete()
        return Response(data={"message": "Delete all products"})


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientNewSerializer

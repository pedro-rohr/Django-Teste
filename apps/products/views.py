from django.shortcuts import render

# Create your views here.

from .models import Product
from rest_framework import viewsets
from .serializer import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

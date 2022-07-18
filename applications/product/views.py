from rest_framework.generics import *
from django.shortcuts import render

from applications.product.models import Product
from applications.product.serializers import ProductSerializer


class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serilalizer_class = ProductSerializer



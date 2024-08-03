from django.shortcuts import render

from rest_framework import viewsets

from .models import ProductCategory,ProductItem
from .serializers import ProductCategorySerializer,ProductItemSerializer
from core.pagination import CustomPagination
# Create your views here.
class ProductCategoryView(viewsets.ModelViewSet):
    queryset=ProductCategory.objects.all()
    serializer_class=ProductCategorySerializer
    
class ProductItemView(viewsets.ModelViewSet):
    queryset=ProductItem.objects.all()
    serializer_class=ProductItemSerializer
    pagination_class = CustomPagination
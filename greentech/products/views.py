from django.shortcuts import render

from django.db.models import Q

from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import ProductCategory,ProductItem
from .serializers import ProductCategorySerializer,ProductItemSerializer
from core.pagination import CustomPagination
# Create your views here.
class ProductCategoryView(viewsets.ModelViewSet):
    queryset=ProductCategory.objects.all()
    serializer_class=ProductCategorySerializer
    pagination_class = None
    
class ProductItemView(viewsets.ModelViewSet):
    queryset=ProductItem.objects.all()
    serializer_class=ProductItemSerializer
    pagination_class = CustomPagination
    
    def list(self,request):
        try:
            search_param=request.query_params.get('category',None)

            if search_param:
                queryset=ProductItem.objects.filter(category_id=search_param)
            else:
                queryset=ProductItem.objects.all() 
                  
            serializer=ProductItemSerializer(queryset,many=True)    

            return Response({"error": False, "rows": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
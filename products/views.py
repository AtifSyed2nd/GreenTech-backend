from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from django.http import FileResponse, Http404
from .models import ProductCategory,ProductItem
from .serializers import ProductCategorySerializer,ProductItemSerializer
from core.pagination import CustomPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class ProductCategoryView(viewsets.ModelViewSet):
    queryset=ProductCategory.objects.all()
    serializer_class=ProductCategorySerializer
    # pagination_class = None
    
class ProductItemView(viewsets.ModelViewSet):
    queryset=ProductItem.objects.all()
    serializer_class=ProductItemSerializer
    pagination_class = CustomPagination
    
    @action(detail=True, methods=['get'])
    def download_brochure(self, request, pk=None):
        item = get_object_or_404(ProductItem, pk=pk)
        if not item.brochure:
            return Response({'error': 'Brochure file not found'}, status=status.HTTP_404_NOT_FOUND)

        response = FileResponse(item.brochure, as_attachment=True)
        response['Content-Type'] = 'application/octet-stream'  # Use generic MIME type for files
        response['Content-Disposition'] = f'attachment; filename="{item.brochure.name}"'
        return response

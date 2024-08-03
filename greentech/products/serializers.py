from rest_framework import serializers

from .models import ProductCategory,ProductItem

class ProductCategorySerializer(serializers.ModelSerializer):
    # image=serializers.ImageField(use_url=False)
    class Meta:
        model=ProductCategory
        fields='__all__'
        

class ProductItemSerializer(serializers.ModelSerializer):
    # image=serializers.ImageField(use_url=False)
    class Meta:
        model=ProductItem
        fields='__all__'
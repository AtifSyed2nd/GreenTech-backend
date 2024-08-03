from django.contrib import admin
from .models import ProductCategory, ProductItem

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(ProductItem)

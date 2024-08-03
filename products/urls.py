from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import (
    ProductCategoryView,
    ProductItemView
)

router=DefaultRouter()
router.register(r'category/nt',ProductCategoryView)
router.register(r'item/nt',ProductItemView)

urlpatterns = [
    path('', include(router.urls))
]

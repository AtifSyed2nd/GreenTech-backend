from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import (
    CardView,
    CarouselView
)

router=DefaultRouter()
router.register(r'card/nt',CardView)
router.register(r'carousel/nt',CarouselView)

urlpatterns = [
    path('', include(router.urls))
]

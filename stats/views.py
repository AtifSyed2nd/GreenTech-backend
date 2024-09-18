from django.shortcuts import render

from rest_framework import viewsets

from .models import Carousel,Card
from .serializers import CardSerializer,CarouselSerializer
from core.pagination import CustomPagination
# Create your views here.
class CardView(viewsets.ModelViewSet):
    queryset=Card.objects.all()
    serializer_class=CardSerializer
    # pagination_class = None
    
class CarouselView(viewsets.ModelViewSet):
    queryset=Carousel.objects.all()
    serializer_class=CarouselSerializer

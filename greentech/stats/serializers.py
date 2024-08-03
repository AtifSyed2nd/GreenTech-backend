from rest_framework import serializers

from .models import Carousel,Card

class CarouselSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carousel
        fields='__all__'
        
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model=Card
        fields='__all__'
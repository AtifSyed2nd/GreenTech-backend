from django.db import models
import uuid

# Create your models here.
def carousel_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/carousel_images/<filename>
    return f'carousel_images/{filename}'

def card_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/carousel_images/<filename>
    return f'card_images/{filename}'

class Carousel(models.Model):
    carousel_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    is_active = models.BooleanField(default=False)  # Whether the category is active
    carousel_remark = models.CharField(max_length=160, null=True, blank=True)
    image = models.ImageField(upload_to=carousel_image_path, null=True, blank=True)  # Image associated with the category
    createdAt = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    
class Card(models.Model):
    card_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    card_title = models.CharField(max_length=160, null=True, blank=True)  # Title of the card
    card_desc=models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)  # Whether the category is active
    image = models.ImageField(upload_to=card_image_path, null=True, blank=True)  # Image associated with the category
    createdAt = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
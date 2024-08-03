from django.db import models
import uuid

# Create your models here.
def category_image_path(instance, filename):
    # File will be uploaded to MEDIA_ROOT/category_images/<filename>
    return f'category_images/{filename}'

class ProductCategory(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4, primary_key=True)  # Unique ID for each category
    category_title = models.CharField(max_length=160, null=True, blank=True)  # Title of the category
    category_desc=models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)  # Whether the category is active
    image = models.ImageField(upload_to=category_image_path, null=True, blank=True)  # Image associated with the category
    createdAt = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    
    def __str__(self):
        return str(self.category_title)  # String representation of the category
    
class ProductItem(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,related_name='category')
    item_id = models.UUIDField(default=uuid.uuid4, primary_key=True)  # Unique ID for each item
    item_title = models.CharField(max_length=160, null=True, blank=True)  # Title of the item
    item_desc=models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=False)  # Whether the item is active
    image = models.ImageField(upload_to=category_image_path, null=True, blank=True)  # Image associated with the item
    createdAt = models.DateTimeField(auto_now_add=True)  # Timestamp of item
    
    def __str__(self):
        return str(self.item_title)  # String representation of the item
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

class CustomUser(AbstractUser):
    user_id = models.UUIDField(default=uuid.uuid4,primary_key=True)
    username=models.CharField(max_length=255,unique=True)
    email= models.EmailField(max_length=255)
    is_superuser = models.BooleanField(default=True)

    
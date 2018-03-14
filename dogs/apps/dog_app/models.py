from django.db import models
from datetime import datetime

# Create your models here.

class Dog(models.Model):
    name = models.CharField(max_length = 45)
    breed = models.CharField(max_length = 45)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)



from django.db import models
from django.utils import timezone

class Contact(models.Model):
    firstName =  models.CharField(max_length=50)
    lastName =  models.CharField(max_length=50, blank=True)
    phone =  models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True)
    createDate = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
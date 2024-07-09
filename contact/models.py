from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name
    
class Contact(models.Model):
    firstName =  models.CharField(max_length=50)
    lastName =  models.CharField(max_length=50, blank=True)
    phone =  models.CharField(max_length=50)
    email = models.EmailField(max_length=250, blank=True)
    createDate = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=False)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/%d')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.category} - {self.firstName}'

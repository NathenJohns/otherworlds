from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

class Category(models.Model):
    category = models.CharField(max_length=40)

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category
        
class Product(models.Model):
    category = models.ForeignKey('Category', default="", on_delete=models.CASCADE)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    image_1 = models.ImageField(upload_to='images', default = "")
    image_2 = models.ImageField(upload_to='images', default = "", blank=True)
    image_3 = models.ImageField(upload_to='images', default = "", blank=True)
    image_4 = models.ImageField(upload_to='images', default = "", blank=True)
    image_5 = models.ImageField(upload_to='images', default = "", blank=True)
    image_6 = models.ImageField(upload_to='images', default = "", blank=True)
    
    class Meta:
        ordering = ['name']
        
    def __unicode__(self):
        return self.name
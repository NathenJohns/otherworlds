from django.db import models
import django_filters

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    category = models.ManyToManyField(Categories, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_main = models.ImageField(upload_to='images')
    image_2 = models.ImageField(upload_to='images', default = "")
    image_3 = models.ImageField(upload_to='images', default = "")
    image_4 = models.ImageField(upload_to='images', default = "")
    image_5 = models.ImageField(upload_to='images', default = "")
    image_6 = models.ImageField(upload_to='images', default = "")
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category
        
class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    category = models.ManyToManyField(Categories, related_name='products')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name
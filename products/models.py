from django.db import models

# Create your models here.

#class Category(models.Model):
#    name = models.CharField(max_length=200, default='')
#    slug = models.SlugField()
    
#    def __str__(self):
#        return self.name
        
class Product(models.Model):
    #category = models.ForeignKey(Category, related_name="products", null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    #created = models.DateTimeField(auto_now_add=True, auto_now=False)
    #updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name
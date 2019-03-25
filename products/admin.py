from django.contrib import admin
from .models import Product, Categories

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
    
admin.site.register(Categories, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    
    search_fields = ['name', 'description', 'price', 'category__category']
    list_display = ['name', 'price', 'available', 'stock']
    list_editable = ['price', 'available', 'stock']
    list_filter = ['price', 'available', 'category__category']
    
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description' , 'price']
    list_display = ['name', 'price', 'available', 'stock']
    list_editable = ['price', 'available', 'stock']
    list_filter = ['price', 'available']
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)
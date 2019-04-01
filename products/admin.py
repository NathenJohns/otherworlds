from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created']
    list_filter = ['price', 'available', 'category__category', 'created']
    list_editable = ['price', 'available']
    search_fields = ['name', 'description', 'price', 'category']
admin.site.register(Product, ProductAdmin)
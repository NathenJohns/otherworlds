from django.contrib import admin
from .models import Product #Category

# Register your models here.

#class CategoryAdmin(admin.ModelAdmin):
#    list_display = ['name', 'slug']
#    prepopulated_fields = {'slug': ('name',)}
#admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'description' , 'price']
    list_display = ['name', 'price', 'available', 'stock']
    list_editable = ['price', 'available', 'stock']
    list_filter = ['price', 'available']
    #prepopulated_fields = {'slug': ('name',)}
    
    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
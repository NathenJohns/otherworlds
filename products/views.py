from django.shortcuts import render
from .models import Product, Categories
from django.views import generic

# Create your views here.
def all_products(request):
    products = Product.objects.all()

    return render(request, "products.html", {"products": products})
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product-detail.html'
    
    
    

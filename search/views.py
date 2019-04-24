from django.shortcuts import *
from django.db.models import Q
from products.models import Product, Category
from django.contrib import messages
from django.core.urlresolvers import reverse

# Create your views here.

def do_search(request):
    
    query_term = request.GET['q']
    products = Product.objects.filter(Q(name__icontains=query_term) | Q(description__icontains=query_term) | Q(category__category__icontains=query_term))

    if products:
        return render(request, "products.html", {"products": products})
        
    else:
        messages.error(request, "This product/category does not exist, please search again.")
        return redirect(reverse('products'))
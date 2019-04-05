from django.shortcuts import *
from .models import Product, Category
from django.views import generic
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def all_products(request):
    products_list = Product.objects.all()
    
    paginator = Paginator(products_list, 8)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
        
    try:
        products = paginator.page(page)
    except(EmptyPage, InvalidPage):
        prodcuts = page(paginator.num_pages)
    
    return render(request, "products.html", {"products": products})
    
class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'product-detail.html'
from django.conf.urls import url, include
from .views import all_products, ProductDetailView

urlpatterns = [
    url(r'^products$', all_products, name='products'),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailView.as_view(), name='product-detail')
]
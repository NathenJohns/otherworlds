from django.conf.urls import url, include
from .views import policies, faq, reviews, contact

urlpatterns = [
    url(r'^policies/$', policies, name='policies'),
    url(r'^faq/$', faq, name='faq'),
    url(r'^reviews/$', reviews, name='reviews'),
    url(r'^contact$', contact, name='contact')
]
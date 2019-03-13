from django.conf.urls import url, include
from .views import FaqPolicies, reviews, contact

urlpatterns = [
    url(r'^policies/$', FaqPolicies, name='policies'),
    url(r'^faq/$', FaqPolicies, name='faq'),
    url(r'^reviews/$', reviews, name='reviews'),
    url(r'^contact$', contact, name='contact')
]
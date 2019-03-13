from django.shortcuts import render

# Create your views here.
def FaqPolicies(request):
    return render(request, "faq-policies.html")
    
def reviews(request):
    return render(request, "reviews.html")

def contact(request):
    return render(request, "contact.html")
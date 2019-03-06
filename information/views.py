from django.shortcuts import render

# Create your views here.
def policies(request):
    return render(request, "policies.html")
    
def faq(request):
    return render(request, "faq.html")
    
def reviews(request):
    return render(request, "reviews.html")

def contact(request):
    return render(request, "contact.html")
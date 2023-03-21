from django.shortcuts import render

def home(request):
    return render(request, 'category.html')
def contact(request):
    return render(request, 'contact.html')
def index(request):
    return render(request, 'index.html')
def list(request):
    return render(request, 'listing.html')

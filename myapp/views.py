from django.views import View
from django.shortcuts import render
from myapp.models import Product

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

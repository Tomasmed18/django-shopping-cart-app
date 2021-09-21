from django.http.response import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse('This is shoppingcart App')

def get_all_products(request):
    all_products = Product.objects.all()
    output = ', '.join([p.name for p in all_products])
    return HttpResponse(output)

def get_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return HttpResponse(product)
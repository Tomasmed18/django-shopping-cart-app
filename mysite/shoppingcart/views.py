from django.http.response import HttpResponse
from .models import Product
from django.shortcuts import get_object_or_404, render

def index(request):
    return HttpResponse('This is shoppingcart App')

def get_all_products(request):
    all_products = Product.objects.all()
    return render(request, 'shoppingcart/all-products.html', {'product_list': all_products})

def get_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shoppingcart/product-detail.html', {'product': product})
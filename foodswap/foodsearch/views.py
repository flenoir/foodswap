from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Hello this si foodsearch app")

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'foodsearch/detail.html', {'product': product, 'code': product.product_code})    

def list_products(request):
    full_list = Product.objects.all()[:5]    
    context = {
        'full_list' : full_list
    }
    return render(request, 'foodsearch/index.html', context)
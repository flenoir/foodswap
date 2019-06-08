# from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.

def index(request):
    return HttpResponse("Hello this si foodsearch app")

def detail(request, product_id):
    return HttpResponse("the product id is %s" % product_id)

def list_products(request):
    full_list = Product.objects.all()[:5]
    output = " , ".join([p.product_name for p in full_list])
    return HttpResponse(output)
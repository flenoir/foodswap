from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from foodsearch.search_form import SearchForm

from .models import Product

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("post")
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['post']
            return render(request, 'foodsearch/index.html', {'form': form, 'data': data })

    form = SearchForm()
    return render(request, 'foodsearch/index.html', {'form': form})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'foodsearch/detail.html', {'product': product, 'code': product.product_code})    

def list_products(request):
    full_list = Product.objects.all()[:5]    
    context = {
        'full_list' : full_list
    }
    return render(request, 'foodsearch/list_products.html', context)

# def get(request):
#     form = SearchForm()
#     return render(request, 'foodsearch/index.html', {'form': form})
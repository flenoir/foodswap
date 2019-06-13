from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from search.search_form import SearchForm
from django.contrib.auth.decorators import login_required

from .models import Product

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("post")
        form = SearchForm(request.POST) # instanciation de l'objet formulaire avec les données de l'objet de la requête
        if form.is_valid():
            data = form.cleaned_data['post']
            db_res = Product.objects.filter(product_name__contains=data)
            res = [i.product_name for i in db_res]
            print(res)

            return render(request, 'search/index.html', {'form': form, 'res': res })

    form = SearchForm()
    return render(request, 'search/index.html', {'form': form})

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'search/detail.html', {'product': product, 'code': product.product_code})    

@login_required
def list_products(request):
    full_list = Product.objects.all()[:5]    
    context = {
        'full_list' : full_list
    }
    return render(request, 'search/list_products.html', context)

# def get(request):
#     form = SearchForm()
#     return render(request, 'search/index.html', {'form': form})
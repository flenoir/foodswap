from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from search.search_form import SearchForm
from django.contrib.auth.decorators import login_required
from stop_words import get_stop_words
from django.db.models import Q

from .models import Product

# Create your views here.

def index(request):
    if request.method == 'POST':
        print("post")
        form = SearchForm(request.POST) # instanciation de l'objet formulaire avec les données de l'objet de la requête
        if form.is_valid():
            data = form.cleaned_data['post']

            stop_words = get_stop_words('fr')
            splited_search = data.split(" ")
            resulting_search = list(set(splited_search) - set(stop_words))
            
            db_res = words_filter(resulting_search)
            res = [i for i in db_res]
                       
            print(res)       
            return render(request, 'search/index.html', {'form': form, 'res': res })

    form = SearchForm()
    return render(request, 'search/index.html', {'form': form})


def words_filter(resulting_search):
    """ filter the number of words in search with AND"""    
    if len(resulting_search) < 2:
        result = Product.objects.filter(product_name__contains=resulting_search[0])
        return result
    elif len(resulting_search) < 3:
        result = Product.objects.filter(product_name__contains=resulting_search[0]).filter(product_name__contains=resulting_search[1])
        return result
    elif len(resulting_search) < 4:
        result = Product.objects.filter(product_name__contains=resulting_search[0]).filter(product_name__contains=resulting_search[1]).filter(product_name__contains=resulting_search[2])
        return result
    elif len(resulting_search) < 5:
        result = Product.objects.filter(product_name__contains=resulting_search[0]).filter(product_name__contains=resulting_search[1]).filter(product_name__contains=resulting_search[2]).filter(product_name__contains=resulting_search[3])
        return result



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
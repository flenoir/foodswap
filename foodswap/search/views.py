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
    """ filter the number of words in search with AND """

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
    json_data = {'product': product, 'code': product.product_code, 'nova_groups': product.nova_groups, 'categories': product.categories, 'nutriscore': product.nutriscore.capitalize()}
    return render(request, 'search/detail.html', json_data)

def swap(request, product_id):
    """ 
    get categories form request
    search database for products matching all categories and with nutriscore corresponding to A 
    display food product
    """

    product = get_object_or_404(Product, pk=product_id)
    splited = product.categories.split(",")    
    categories_res = Product.objects.filter(categories__contains=splited[0]).filter(categories__contains=splited[1]).filter(categories__contains=splited[2])
    
    arr = []
    for x in categories_res:        
        z = compare_products(x, product)
        if z is not None:
            arr.append(z)

    if bool(arr) is False:
        substitute = product
        json_data = {'product': substitute, 'code': substitute.product_code, 'nova_groups': substitute.nova_groups, 'categories': substitute.categories, 'nutriscore': substitute.nutriscore.capitalize(), 'status': 'no better product found'}
    else: 
        substitute = arr[0][0]
        print(substitute.product_code)        
        json_data = {'product': substitute, 'code': substitute.product_code, 'nova_groups': substitute.nova_groups, 'categories': substitute.categories, 'nutriscore': substitute.nutriscore.capitalize(), 'status': ''}
   
    return render(request, 'search/swap.html', json_data)


def compare_products(x, y):
    """ compare nutriscores to return better product"""

    abc = ["a","b","c","d","e","f","g"]
    # if x location's index in abc is lower than y location's index then...
    res1 = abc.index(x.nutriscore)
    res2 = abc.index(y.nutriscore)
    print(res1, res2)
    
    if res1 < res2:
        print("better product")        
        return x, x.id
    else:
        print("worse product")
        

@login_required
def list_products(request):
    full_list = Product.objects.all()[:5]    
    context = {
        'full_list' : full_list
    }
    return render(request, 'search/list_products.html', context)
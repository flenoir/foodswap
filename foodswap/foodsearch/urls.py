from django.urls import path

from . import views


# app_name = 'foodsearch'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:product_id>/', views.detail, name='detail'),
    path('list_products/', views.list_products, name='list_products'),
]
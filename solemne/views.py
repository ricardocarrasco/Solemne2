from django.shortcuts import render, redirect

from solemne.models import Marcas, Categorias, Productos

# Create your views here.
def index(request):

    products = Productos.objects.filter(status=1)

    categories = Categorias.objects.filter(status=1)
    
    return render(request, 'index.html', {'products':products, 'categories':categories})

def category(request,category_id):

    products = Productos.objects.filter(category__id=category_id, status=1)

    categories = Categorias.objects.filter(status=1)

    return render(request, 'Categorias.html', {'products':products, 'categories':categories})


def product(request,product_id):
    products = Productos.objects.filter(id=product_id, status=1)

    return render(request, 'Productos.html', {'products':products})    
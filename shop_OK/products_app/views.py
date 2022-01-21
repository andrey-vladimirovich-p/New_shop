from django.shortcuts import render
from .models import Product, CategoryProduct


def index(request):
    category = None
    categories = CategoryProduct.objects.all()
    products = Product.objects.filter(available=True)

    return render(request,
                  'index.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_list(request):
    category = None
    categories = CategoryProduct.objects.all()
    products = Product.objects.filter(available=True)

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})
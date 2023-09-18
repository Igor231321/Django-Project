from django.shortcuts import render
from .models import Product


def index_page(request):
    """Домашняя страница"""
    return render(request, 'product/index.html', {'products': Product.objects.all()})

from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic 

from .models import Product

class IndexView(generic.ListView):
    model = Product
    template_name = "product/index.html"
    context_object_name = "product_list"
    
    def get_queryset(self):
        return Product.objects.all()[:3]
    

class DetailView(generic.DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = "product"

class AllProductView(generic.ListView):
    model = Product
    template_name = "product/all_product.html"
    context_object_name = "product_list"
    
    def get_queryset(self):
        return Product.objects.all()
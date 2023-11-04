from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Product


class IndexView(generic.ListView):
    model = Product
    template_name = "product/index.html"
    context_object_name = "product_list"
    
    def get_queryset(self):
        return Product.published.all()[:3]
    

# class DetailView(generic.DetailView):
#     model = Product
#     template_name = "product/detail.html"
#     context_object_name = "product"


def show_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, 'product/detail.html', {"product": product})


class AllProductView(generic.ListView):
    model = Product
    template_name = "product/all_product.html"
    context_object_name = "product_list"
    
    def get_queryset(self):
        return Product.objects.all()
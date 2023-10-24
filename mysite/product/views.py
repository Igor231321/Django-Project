from django.shortcuts import render, get_object_or_404
from django.views import generic 

from .models import Product

class IndexView(generic.ListView):
    template_name = "product/index.html"
    context_object_name = "product_list"
    
    def get_queryset(self):
        return Product.objects.all()[:3]
    
class DetailView(generic.DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = "product"
    
# def detail(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, "product/detail.html", {"product": product})
from django.views import generic
from django.shortcuts import render, get_object_or_404

from .models import Product, Category
            
# class IndexView(generic.ListView):
#     """Выводит 3 карточки товара."""
#     model = Product
#     template_name = "product/index.html"
#     context_object_name = "product_list"

#     def get_queryset(self):
#         return Product.published.all()[:3]

def index_page(request):
    products = Product.published.all()[:3]
    context = {"product_list": products,}
    
    return render(request, "product/index.html", context)

# class DetailView(generic.DetailView):
#     model = Product
#     template_name = "product/detail.html"
#     context_object_name = "product"

def show_product(request, product_slug):
    """Выводит один товар."""
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, "product/detail.html", {"product": product})


class AllProductView(generic.ListView):
    """Выводит весь товар."""

    model = Product
    template_name = "product/all_product.html"
    context_object_name = "product_list"

    def get_queryset(self):
        return Product.objects.all()


def show_category(request, category_slug):
    """Выводит одну категорию отобраною по короткой метке (Slug)."""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.published.filter(category_id=category)
    
    return render(request, "product/index.html", {"category": category, 
                                                  "products": products})


def buy_page(request, product_slug):
    """Выводит форму по отдельному товару."""
    product = get_object_or_404(Product, slug=product_slug)
    content = {"product": product}
    
    return render(request, "product/buy_product.html", content)
    
from django.views import generic
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage
from .models import Product, Category

# class IndexView(generic.ListView):
#     """Выводит 3 карточки товара."""
#     model = Product
#     template_name = "product/index.html"
#     context_object_name = "product_list"
#     queryset = Product.published.all()[:3]


def index_page(request):
    products = Product.published.all()[:3]
    context = {
        "product_list": products,
    }

    return render(request, "product/index.html", context)


# class DetailView(generic.DetailView):
#     model = Product
#     template_name = "product/detail.html"
#     context_object_name = "product"


def detail_product(request, product_slug):
    """Выводит один товар."""
    product = get_object_or_404(Product, slug=product_slug)
    return render(request, "product/detail.html", {"product": product})

# class ProductListView(generic.ListView):
#     model = Product
#     queryset = Product.published.all()
#     context_object_name = 'products'
#     paginate_by = 3
#     template_name = 'product/all_product.html'


def product_list(request):
    product_list = Product.published.all()
    paginator = Paginator(product_list, 2)
    page_number = request.GET.get("page", 1)
    try:
        products = paginator.page(page_number)
    except EmptyPage:
        # if page_number has don't diaposon, get last page
        products = paginator.page(paginator.num_pages)
    return render(request, "product/all_product.html", {"products": products})


def detail_category(request, category_slug):
    """Выводит одну категорию отобраною по короткой метке (Slug)."""
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.published.filter(category_id=category)
    return render(
        request, "product/index.html", {"category": category, "products": products}
    )


def buy_page(request, product_slug):
    """Выводит форму по отдельному товару."""
    product = get_object_or_404(Product, slug=product_slug)
    content = {"product": product}
    return render(request, "product/buy_product.html", content)

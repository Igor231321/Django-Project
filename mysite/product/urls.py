from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    # home page
    # path("", views.IndexView.as_view(), name="index"),
    path("", views.index_page, name="index"),
    # product_detail
    # path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("detail/<slug:product_slug>/", views.detail_product, name="detail"),
    # show_all_product
    path("all_product/", views.product_list, name="all_product"),
    # show_category
    path("category/<slug:category_slug>/", views.detail_category, name="category"),
    # buy form
    path("detail/<slug:product_slug>/buy", views.buy_page, name="buy_menu"),
]

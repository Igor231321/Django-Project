from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    # Главная страница
    path("", views.IndexView.as_view(), name="index"),
    # detail/pk_product
    path("detail/<int:pk>/", views.DetailView.as_view(), name="detail"),
]

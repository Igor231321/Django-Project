from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Подключени модуля product.urls (Основного приложеия)
    path("", include('product.urls')),
    # Админка
    path("admin/", admin.site.urls),
]




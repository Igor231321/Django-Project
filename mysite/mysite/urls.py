from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # Подключение модуля polls.urls (Первого приложения)
    path("", include('polls.urls')),
    # Админка
    path("admin/", admin.site.urls),
]




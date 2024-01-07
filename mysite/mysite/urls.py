from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Подключени модуля product.urls (Основного приложеия)
    path("", include('product.urls')),
    # Админка
    path("admin/", admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



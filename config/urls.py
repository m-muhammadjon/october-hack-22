from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from config.routing import urlpatterns as api_urls
from config.swagger import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += swagger_urls
urlpatterns += api_urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

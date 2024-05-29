from urllib import request
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import settings
from core.settings import MEDIA_URL, MEDIA_ROOT
import cinema.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cinema.urls)),
]

if settings.DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

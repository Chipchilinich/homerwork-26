
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls', namespace='catalogs')),
    path('contacts/', include('catalog.urls', namespace='contacts')),
    path('', include('catalog.urls', namespace='catalog')),
    path('', include('blog.urls', namespace='blog')),
    path('users/', include('users.urls', namespace='users')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


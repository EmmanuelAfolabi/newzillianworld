from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', include('homes.urls')),
    path('store/', include('store.urls')),
    path('aquarium/', include('aquarium.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "ZillianWorld "
admin.site.site_title = "ZillianWorld Admin"
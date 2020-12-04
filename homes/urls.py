from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('homes', views.homes, name='homes'),
    path('contact', views.contact_us, name='contact'),
    path('search', views.search, name='search'),
    path('about', views.about, name='about'),
    path('home_single/<int:pk>/', views.home_single, name='home_single'),
    path('subscribe', views.subscriber, name='subscribe'),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

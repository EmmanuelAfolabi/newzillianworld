from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.aquarium, name='aquarium'),
    path('aquarium_single/<int:pk>/', views.aquarium_single, name='aquarium_single'),
    path('aquarium_cart', views.aquarium_bag, name='aquarium_cart'),
    path('aquarium_checkout', views.aquarium_checkout, name='aquarium_checkout'),
    path('update_item', views.aquarium_updateItem, name='update_item'),
    path('process_order', views.aquarium_processOrder, name='process_order'),
    path('search', views.search, name='search'),
    path('subscribe', views.subscriber, name='subscribe'),

]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

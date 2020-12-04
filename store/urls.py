from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.store, name='store'),
    path('store_single/<int:pk>/', views.store_single, name='store_single'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('store_search', views.search, name='store_search'),
    path('update_item', views.updateItem, name='update_item'),
    path('process_order', views.processOrder, name='process_order'),
    path('subscribe', views.subscriber, name='subscribe'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

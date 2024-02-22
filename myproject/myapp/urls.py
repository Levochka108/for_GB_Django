from django.urls import path
from . import views
from .views import product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Оставьте только один маршрут с опциональным customer_id
    path('products/', views.product_list, name='product_list'), # Этот маршрут будет обрабатывать оба случая
    # Удалите или закомментируйте строку ниже, чтобы избежать дублирования
    path('create-product/', views.create_product_view, name='create_product'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
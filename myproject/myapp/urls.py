from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    # Оставьте только один маршрут с опциональным customer_id
    path('products/', views.product_list, name='product_list'),  # Этот маршрут будет обрабатывать оба случая
    # Удалите или закомментируйте строку ниже, чтобы избежать дублирования
    # path('products/<int:customer_id>/', views.product_list, name='product_list_with_id')
]
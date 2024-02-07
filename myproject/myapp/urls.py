from django.urls import path
from . import views
from .views import product_list

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),
    path('products/', views.product_list, name='product_list'),
]
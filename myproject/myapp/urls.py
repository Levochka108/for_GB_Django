from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Убедитесь, что это здесь
    path('about/', views.about, name='about'),
]
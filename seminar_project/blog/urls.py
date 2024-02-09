from django.urls import path
from .views import home, article_list, article_detail

urlpatterns = [
    path('', home, name='home'),  # Главная страница
    path('articles/', article_list, name='article_list'),  # Список статей
    path('article/<int:pk>/', article_detail, name='article_detail'),  # Просмотр одной статьи
]

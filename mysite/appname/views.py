from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import logging

# Настройка логгера
logger = logging.getLogger(__name__)

def home(request):
    logger.info("Посещение главной страницы")
    html = "<h1>Добро пожаловать на мой первый сайт на Django!</h1>"
    return HttpResponse(html)

def about(request):
    logger.info("Посещение страницы 'О себе'")
    html = "<h1>О себе</h1><p>Здесь некоторая информация обо мне...</p>"
    return HttpResponse(html)

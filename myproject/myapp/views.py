from django.shortcuts import render
import logging
from django.shortcuts import render
from django.templatetags.static import static
from .models import Product

# Create your views here.
# Настраиваем логирование
logger = logging.getLogger(__name__)

def home(request):
    context = {
        'background_image_url': static('images/welcome.jpg')  
    }
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def product_list(request):
    products = Product.objects.all()  # Извлекаем все продукты
    return render(request, 'myapp/product_list.html', {'products': products})
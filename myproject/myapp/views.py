from django.shortcuts import render
import logging
from django.shortcuts import render
from django.templatetags.static import static


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

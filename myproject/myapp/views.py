from django.shortcuts import render
import logging
from django.shortcuts import render
from django.templatetags.static import static
from datetime import date, timedelta
from django.shortcuts import get_object_or_404, render
from .models import Article
from .models import Customer, Order


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

def product_list(request, customer_id=None):
    today = date.today()
    week_delta = today - timedelta(days=7)
    month_delta = today - timedelta(days=30)
    year_delta = today - timedelta(days=365)
  
    user = Customer.objects.get(id=customer_id)
    orders_week = Order.objects.filter(client=user, order_date__gte=week_delta).all()
    orders_month = Order.objects.filter(client=user, order_date__gte=month_delta).all()
    orders_year = Order.objects.filter(client=user, order_date__gte=year_delta).all()
    context = {
        'orders_week': orders_week,
        'orders_month': orders_month,
        'orders_year': orders_year,
    }

    return render(request, 'myapp/product_list.html', context)

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.order_by('created_date')
    return render(request, 'blog/article_detail.html', {'article': article, 'comments': comments})

def customer_orders(request, customer_id):
    orders = Order.objects.filter(customer_id=customer_id).prefetch_related('products')
    return render(request, 'shop/customer_orders.html', {'orders': orders})
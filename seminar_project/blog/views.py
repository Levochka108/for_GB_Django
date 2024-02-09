from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.shortcuts import render
from .models import Order
from django.utils import timezone


def home(request):
    return HttpResponse("Welcome to the seminar project home page!")


def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article_detail.html', {'article': article})

def get_products_from_orders(orders):
    products_set = set()
    for order in orders:
        for product in order.products.all():
            products_set.add(product)
    return list(products_set)

def ordered_products(request):
    enddate = timezone.now()
    startdate_week = enddate - timedelta(days=7)
    startdate_month = enddate - timedelta(days=30)
    startdate_year = enddate - timedelta(days=365)

    week_orders = Order.objects.filter(customer=request.user, order_date__range=[startdate_week, enddate])
    month_orders = Order.objects.filter(customer=request.user, order_date__range=[startdate_month, enddate])
    year_orders = Order.objects.filter(customer=request.user, order_date__range=[startdate_year, enddate])

    week_products = get_products_from_orders(week_orders)
    month_products = get_products_from_orders(month_orders)
    year_products = get_products_from_orders(year_orders)

    return render(request, 'shop/ordered_products.html', {
        'week_products': week_products,
        'month_products': month_products,
        'year_products': year_products,
    })
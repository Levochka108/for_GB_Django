
from django.db import models
from django.utils.timezone import now, timedelta
from shop.models import Product, Customer



class Article(models.Model):
    # Определение полей модели
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.article}"
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='blog_orders', on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='blog_orders')
    order_date = models.DateTimeField(auto_now_add=True)

def ordered_products(request):
    enddate = now()
    startdate_week = enddate - timedelta(days=7)
    startdate_month = enddate - timedelta(days=30)
    startdate_year = enddate - timedelta(days=365)

    week_orders = Order.objects.filter(customer=request.user, order_date__range=[startdate_week, enddate])
    month_orders = Order.objects.filter(customer=request.user, order_date__range=[startdate_month, enddate])
    year_orders = Order.objects.filter(customer=request.user, order_date__range=[startdate_year, enddate])

    # Для упрощения, предполагаем, что у нас есть функция get_products_from_orders, которая извлекает товары из заказов
    week_products = get_products_from_orders(week_orders)
    month_products = get_products_from_orders(month_orders)
    year_products = get_products_from_orders(year_orders)

    return render(request, 'ordered_products.html', {
        'week_products': week_products,
        'month_products': month_products,
        'year_products': year_products,
    })


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name
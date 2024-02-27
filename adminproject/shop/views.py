from django.views.generic import ListView, DetailView
from .models import Client, Product, Order


class ClientListView(ListView):
    model = Client
    template_name = 'shop/client_list.html'  # Указываем шаблон для списка клиентов


class ClientDetailView(DetailView):
    model = Client
    # Указываем шаблон для деталей клиента
    template_name = 'shop/client_detail.html'


class ProductListView(ListView):
    model = Product
    # Указываем шаблон для списка продуктов
    template_name = 'shop/product_list.html'


class ProductDetailView(DetailView):
    model = Product
    # Указываем шаблон для деталей продукта
    template_name = 'shop/product_detail.html'


class OrderListView(ListView):
    model = Order
    template_name = 'shop/order_list.html'  # Указываем шаблон для списка заказов


class OrderDetailView(DetailView):
    model = Order
    template_name = 'shop/order_detail.html'  # Указываем шаблон для деталей заказа

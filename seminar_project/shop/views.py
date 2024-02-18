from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Order

def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'shop/order_list.html', {'orders': orders})

class OrderListView(ListView):
    model = Order
    template_name = 'shop/order_list.html'

    def get_queryset(self):
        """Вернуть заказы текущего пользователя."""
        return Order.objects.filter(customer=self.request.user)\
    
class OrderDetailView(DetailView):
    model = Order
    template_name = 'shop/order_detail.html'

    def get_queryset(self):
        """Вернуть детали заказа для текущего пользователя."""
        return Order.objects.filter(customer=self.request.user)
    

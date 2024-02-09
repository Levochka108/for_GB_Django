from django.shortcuts import render
from .models import Order

def order_list(request):
    orders = Order.objects.filter(customer=request.user)
    return render(request, 'shop/order_list.html', {'orders': orders})

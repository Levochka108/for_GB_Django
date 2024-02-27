
from django.urls import path
from . import views

urlpatterns = [

    path('', views.WelcomeView.as_view(), name='welcome'),
    path('customers/', views.CustomerListView.as_view(), name='customer-list'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('orders/', views.OrderListView.as_view(), name='order-list'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(),
         name='customer-detail'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(),
         name='product-detail'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order-detail'),
]

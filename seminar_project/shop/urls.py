from django.contrib import admin
from django.urls import path, include  # Импортируйте include
from .views import ordered_products, CustomerListView, ProductListView, OrderListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Включите URL-маршруты приложения blog
    path('ordered-products/', ordered_products, name='ordered-products'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]

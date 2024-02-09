from django.contrib import admin
from django.urls import path, include  # Импортируйте include
from .views import ordered_products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),  # Включите URL-маршруты приложения blog
    path('ordered-products/', ordered_products, name='ordered-products'),
]

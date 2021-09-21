from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product/all', views.get_all_products, name='all products'),
    path('product/<int:product_id>', views.get_product, name='get product'),
]
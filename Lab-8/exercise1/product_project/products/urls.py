from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Define URL pattern for the index page
    path('add_product/', views.add_product, name='add_product'),  # Define URL pattern for the add_product page
    path('product_list/', views.product_list, name='product_list'),  # Define URL pattern for the product_list page
]

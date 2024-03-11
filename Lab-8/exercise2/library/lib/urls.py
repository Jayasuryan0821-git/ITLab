from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('author/create/', views.author_create, name='author_create'),
    path('publisher/create/', views.publisher_create, name='publisher_create'),
    path('book/create/', views.book_create, name='book_create'),
    path('display/', views.display_all, name='display_all'),  # Add this line
]

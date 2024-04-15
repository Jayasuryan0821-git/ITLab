from . import views
from django.urls import path
urlpatterns = [
    path('',views.index,name='index'),
    path('author_create',views.author_create,name='author_create'),
    path('publisher_create',views.publisher_create,name='publisher_create'),
    path('book_create',views.book_create,name='book_create'),
    path('display_all',views.display_all,name='display_all')
]
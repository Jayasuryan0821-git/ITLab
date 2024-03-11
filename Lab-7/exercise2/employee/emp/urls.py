
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert-works/', views.index, name='insert_works'),
    path('retrieve-data/', views.index, name='retrieve_data'),
]

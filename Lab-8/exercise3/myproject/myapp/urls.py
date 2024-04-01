# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_human_details/', views.get_human_details, name='get_human_details'),
]

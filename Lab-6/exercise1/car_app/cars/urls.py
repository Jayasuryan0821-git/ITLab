from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.car_form, name='car_form'),
    path('car-details/', views.car_details, name='car_details'),
]

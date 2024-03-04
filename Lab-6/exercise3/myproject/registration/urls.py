# urls.py

from django.urls import path
from .views import register, generate_bill

urlpatterns = [
    path('', register, name='register'),
    path('generate-bill/', generate_bill, name='generate_bill'),
]

from django.urls import path,include
from django.contrib import admin
from .views import student_form

urlpatterns = [
    path('',student_form,name='student_form'),
]
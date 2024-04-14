from django.urls import path,include
from . import views 
urlpatterns = [
    path('',views.index,name="index"),
    path('add_catgeory',views.add_category,name='add_category'),
    path('add_page',views.add_page,name='add_page'),
]
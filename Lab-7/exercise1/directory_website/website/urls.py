from django.urls import path, include
from website import views   # Assuming 'website' is the name of your app

urlpatterns = [
    path('', views.home, name='home'),
    path('add-category/', views.add_category, name='add_category'),
    path('add-page/', views.add_page, name='add_page'),
    path('like-page/<int:page_id>/', views.like_page, name='like_page'),
    path('visit-category/<int:category_id>/', views.visit_category, name='visit_category'),
]

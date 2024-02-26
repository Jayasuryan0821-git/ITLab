from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='first/')),  # Redirect root to first page
    path('first/', include('pages.urls')),  # Include URLs from 'pages' app for first page
    path('second/', include('pages.urls')),  # Include URLs from 'pages' app for second page
]

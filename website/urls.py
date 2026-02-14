from django.urls import path
from .views import index_view, about_view, contact_view, website

urlpatterns = [
    path('home', index_view),
    path('about', about_view),
    path('contact', contact_view),
    path('', website)
]
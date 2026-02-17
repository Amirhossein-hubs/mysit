from django.urls import path
from .views import about_view, contact_view, website

urlpatterns = [
    path('about', about_view),
    path('contact', contact_view),
    path('', website)
]
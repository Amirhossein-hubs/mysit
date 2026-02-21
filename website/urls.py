from django.urls import path
from .views import about_view, contact_view, website, element_view, test_view

app_name = 'website'

urlpatterns = [
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('elements', element_view, name='elements'),
    path('test', test_view, name='test'),
    path('', website, name='index'),
]
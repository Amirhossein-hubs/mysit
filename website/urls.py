from django.urls import path
from .views import about_view, contact_view, website, element_view, test_view, newslatter_views

app_name = 'website'

urlpatterns = [
    path('', website, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('elements', element_view, name='elements'),
    path('newslatter', newslatter_views, name='newslatter'),
    path('test', test_view, name='test'),
]
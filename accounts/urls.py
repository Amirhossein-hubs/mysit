from django.urls import path
from accounts.views import login_views, logout_views, singup_views


app_name = 'accounts'

urlpatterns = [
    path('login', login_views, name='login'),
    path('logout', logout_views, name='logout'),
    path('singup', singup_views, name='singup'),
]
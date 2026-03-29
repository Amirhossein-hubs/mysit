from django.urls import path
from .views import blog_view, blog_single, test_view, blog_search

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='index'),
    path('<int:pid>', blog_single, name='single'),
    path('category/<str:cate_name>', blog_view, name='category'),
    path('tag/<str:tag_name>', blog_view, name='tag'),
    path('author/<str:author_username>', blog_view, name='author'),
    path('search/', blog_search, name='search'),
    path('test', test_view, name='test')
]















#path('<str:name>/<str:family_name>/<int:age>', test, name='test'),
from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name='totalposts')
def function():
    posts = Post.objects.filter(status=True, published_date__lte = timezone.now()).count()
    return posts


@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=True, published_date__lte = timezone.now())
    return posts


@register.filter
def snippet(value,arg=30):
    return value[:arg]

@register.inclusion_tag('blog/popular_posts.html')
def popular_posts():
    posts = Post.objects.filter(status=True, published_date__lte = timezone.now()).order_by('published_date')
    return {'posts':posts}

@register.inclusion_tag('website/latest_post.html')
def latestposts():
    posts = Post.objects.filter(status=True, published_date__lte = timezone.now())[:6]
    return {'posts':posts}

@register.inclusion_tag('blog/post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=True, published_date__lte = timezone.now())
    categories = Category.objects.all()

    cate_dict = {}
    for name in categories:
        cate_dict[name] = posts.filter(category=name).count()
    return {'categories':cate_dict}
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone     #که زمان فعلی را با دقت منطقه زمانی برمی‌گرداند
from blog.models import Post



def blog_view(request,**kwargs):
    posts = Post.objects.filter(published_date__lte = timezone.now(),status=True).order_by('published_date')      #lte = کوچکتر مساوی
    if kwargs.get('cate_name') != None:
        posts = posts.filter(category__name = kwargs['cate_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username = kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name = kwargs['tag_name'])

    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {
        'posts':posts
    }

    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    posts = list(Post.objects.filter(published_date__lte = timezone.now(),status=True).order_by('id'))

    post = get_object_or_404(Post,pk=pid,status=True,published_date__lte = timezone.now())

    current_index = posts.index(post)                                                     #داره ایدی پوست رو داخل لیست تمامی ایدی ها پیدا میکنه و ایندکسش که میشه جایگاه اون ایدی داخل ایدی های دیگه رو پیدا میکنه تا اینکه ایندکس های قبل و بعد یا بهتره بگیم ایدی های قبل بعد پیدا کنیم

    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None
    prev_post = posts[current_index - 1] if current_index > 0 else None
    
    post.counted_views += 1
    post.save()

    context = {
        'posts':post,
        'next_post':next_post,
        'prev_post':prev_post
    }                              

    return render(request, 'blog/blog-single.html', context)


def test_view(request):
    return render(request, 'test.html')

def blog_search(request):
    posts = Post.objects.filter(published_date__lte = timezone.now(),status=True)                                                                                             #print(request.__dict__)
    if request.method == 'GET':                                                                   #request.method  == نوع درخواست رو خروجی میده
        if s := request.GET.get('s'):                                                             #request.GET  ==  مقدار ورودی کاربر (s) از request.GET گرفته می‌شه.
            posts = posts.filter(content__contains=s)                                             #تابع get('s') مقدار django رو برمی‌گردونه.            #request == django
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog-home.html', context)









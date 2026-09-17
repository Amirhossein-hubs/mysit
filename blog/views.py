from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone     #که زمان فعلی را با دقت منطقه زمانی برمی‌گرداند
from blog.models import Post, Comment
from blog.forms import Comment_form
from django.contrib import messages

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
        'posts':posts,
    }

    return render(request, 'blog/blog-home.html', context)

def blog_single(request,pid):
    if request.method == 'POST':
        form = Comment_form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your comment submited successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your comment didnt submited', extra_tags='danger')
    posts = list(Post.objects.filter(published_date__lte = timezone.now(),status=True).order_by('id'))
    post = get_object_or_404(Post,pk=pid,status=True,published_date__lte = timezone.now())
    current_index = posts.index(post)                                                     #داره ایدی پوست رو داخل لیست تمامی ایدی ها پیدا میکنه و ایندکسش که میشه جایگاه اون ایدی داخل ایدی های دیگه رو پیدا میکنه تا اینکه ایندکس های قبل و بعد یا بهتره بگیم ایدی های قبل بعد پیدا کنیم
    next_post = posts[current_index + 1] if current_index < len(posts) - 1 else None
    prev_post = posts[current_index - 1] if current_index > 0 else None
    post.counted_views += 1
    post.save()

    comment = Comment.objects.filter(post=post.id ,approved=True)
    form = Comment_form()

    if post.login_require:
        if not request.user.is_authenticated:
            messages.add_message(request, messages.WARNING, 'برای دیدن این بخش باید لاگین کنید')
            context= {
                'posts':post,
            }
            return render(request, 'accounts/login.html', context)
        else:
            context= {
                'posts':post,
                'next_post':next_post,
                'prev_post':prev_post,
                'form':form,
                'comment':comment,
            }
            return render(request, 'blog/blog-single.html', context)
    else:
        context= {
            'posts':post,
            'next_post':next_post,
            'prev_post':prev_post,
            'form':form,
            'comment':comment,
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









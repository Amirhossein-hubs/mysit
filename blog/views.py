from django.shortcuts import render, get_object_or_404
from blog.models import Post

def blog_view(request):
    posts = Post.objects.filter(status=True)
    return render(request, 'blog/blog-home.html', {'posts':posts})

def blog_single(request,pid):
    posts = get_object_or_404(Post,pk=pid,status=True)                                                                
    return render(request, 'blog/blog-single.html', {'posts':posts})






from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,  HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.utils import timezone
from blog.models import Post
from website.models import Contact
from website.forms import Contact_form, Newslatter_form


def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)                                                       # هنوز ذخیره نشود
            contact.name = "ناشناس"
            contact.save()                                                                          # ذخیره نهایی
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
            return redirect('website:contact')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited', extra_tags='danger')
            return render(request, 'website/contact.html', {'form':form})
    else:
        form = Contact_form()
        return render(request, 'website/contact.html', {'form':form})

def newslatter_views(request):
    if request.method == 'POST':
        form = Newslatter_form(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
            return redirect('website:index')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited', extra_tags='danger')
            return render(request, 'website/index.html')
    else:
        return render(request, 'website/index.html')
            

def element_view(request):
    return render(request, 'website/elements.html')

def website(request):
    return render(request, 'website/index.html')

def test_view(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():                                             #ورودی رو با فیلد چک میکنه ببینه مطاقبت داره یا نه
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('note valid')
        
    form = Contact_form()
    return render(request, 'test.html', {'form':form})




    
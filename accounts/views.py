from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required               #این دکوریتور تایین میکنه که کاربر باید لاگین کرده باشه تا نمایش بده وگرنه به صفحه لاگین میره و تا فرد لاگین نکنه چیزی نمایش نمیده
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



def login_views(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                email = request.POST['email']
            
                try:
                    user_obj = User.objects.get(username=username)
                except User.DoesNotExist:
                    try:
                        user_obj = User.objects.get(email=email)
                    except User.DoesNotExist:
                        messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نمی‌باشد', extra_tags='danger')
                        return render(request, 'accounts/login.html')
        
                user = authenticate(request, username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    messages.add_message(request, messages.SUCCESS, f'خوشامدید {request.user.username}')
                    return redirect('website:index')
                else:
                    messages.add_message(request, messages.ERROR, 'اطلاعات وارد شده صحیح نمیباشد', extra_tags='danger')

        return render(request, 'accounts/login.html')
    else:
        return redirect('/')

@login_required
def logout_views(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    


def singup_views(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            username = request.POST['username']
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'اطلاعات با موفقیت ثبت شد')
                return redirect('accounts:login')
            try:
                User.objects.get(username=username)
                messages.add_message(request, messages.ERROR, 'این نام کاربری وجود دارد', extra_tags='danger')
            
            except User.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'اطلاعات صحیح نیست دوباره تلاش کنید', extra_tags='danger')
                
            
        form = UserCreationForm()
        return render(request, 'accounts/singup.html',{'form':form})
    else:
        messages.add_message(request, messages.WARNING, 'شما ثبتنام کرده اید')
        return redirect('/')




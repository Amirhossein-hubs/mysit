from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def website(request):
    return render(request, 'index.html')
    
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    return render(request, 'website/contact.html')

def element_view(request):
    return render(request, 'website/elements.html')

def website(request):
    return render(request, 'website/index.html')




    
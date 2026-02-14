from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def index_view(request):
    return HttpResponse("<h1>Home Page</h1>")

def about_view(request):
    return JsonResponse({'Name':'amir'})

def contact_view(request):
    return HttpResponse("<h1>contact</h1>")

def website(request):
    return HttpResponse("<h1>my website</h1>")
    
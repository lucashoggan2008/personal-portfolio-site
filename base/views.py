from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/home.html', {'title_name':'Home'})

def about_me(request):
    return render(request, 'base/about-me.html', {"title_name":"About-Me"})

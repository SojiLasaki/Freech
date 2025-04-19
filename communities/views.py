from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, "communities/home.html", context)

def communities(request):
    context = {}
    return render(request, "communities/home.html", context)

def circles(request):
    context = {}
    return render(request, "communities/home.html", context)


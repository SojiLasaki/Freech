from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    page="home"
    communities = Community.objects.all()
    context = {'communities' : communities}
    return render(request, "communities/home.html", context)


def communities(request):
    context = {}
    return render(request, "communities/home.html", context)


def create_community(request):
    context = {}
    return render(request, "communities/home.html", context)


def circles(request):
    context = {}
    return render(request, "communities/home.html", context)


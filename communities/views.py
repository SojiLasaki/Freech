from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def home(request):
    page="home"
    context = {}
    return render(request, "communities/home.html", context)


def communities(request):
    page="communities"
    profile = request.user.profile
    community = profile.community
    communities = Community.objects.all()

    if community:
        return redirect('community')

    context = {'communities' : communities, "community":community}
    return render(request, "communities/communities.html", context)


def community(request):
    profile = request.user.profile
    community = profile.community
    
    if not community:
        return redirect('communities')
    
    context = {'community':community}
    return render(request, "communities/community.html", context)


def request_community(request):
    context = {}
    return render(request, "communities/form.html", context)


def circles(request):
    profile = request.user.profile
    community = profile.community

    if not community:
        return redirect('communities')
    
    context = {'community':community}
    return render(request, "communities/circles.html", context)



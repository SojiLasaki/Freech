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
    page = "community"
    profile = request.user.profile
    community = profile.community
    convos = community.convo_set.all()
    
    if not community:
        return redirect('communities')
    
    context = {'object':community, 'convos':convos, 'page':page}
    return render(request, "communities/community.html", context)


def request_community(request):
    context = {}
    return render(request, "communities/form.html", context)


def circles(request):
    profile = request.user.profile
    circles = profile.circle_set.all()
    # my_circles = 

    if not circles:
        return redirect('circles')
    
    context = {'circles':circles}
    return render(request, "communities/circles.html", context)


def circle(request, pk):
    page = "circle"
    circle = Circle.objects.get(id=pk)
    convos = circle.convo_set.all()
    
    if not community:
        return redirect('circl')
    
    context = {'object':circle, 'convos':convos, 'page':page}
    return render(request, "communities/circle.html", context)

def convo(request, pk):
    profile = request.user.profile
    convo = Convo.objects.get(id=pk)
    community = convo.community
    replies = convo.reply_set.all()
    context = {"convo":convo, 'replies':replies, 'community':community}
    return render(request, "communities/convo.html", context)


def circle_convo(request, pk):
    profile = request.user.profile
    convo = Convo.objects.get(id=pk)
    circle = convo.circle
    replies = convo.reply_set.all()
    context = {"convo":convo, 'replies':replies, "circle":circle}
    return render(request, "communities/convo_circle.html", context)


def create_circle(request):
    context = {}
    return render(request, "communities/form.html", context)


def create_reply(request):
    context = {}
    return render(request, "communities/form.html", context)


def create_convo(request):
    context = {}
    return render(request, "communities/form.html", context)
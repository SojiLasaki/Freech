from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.urls import conf
from django.db.models import Q
from .models import *
from .forms import *
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import HttpResponseBadRequest
# Create your views here.


@login_required(login_url ='login')
def profile(request):
    profile = request.user.profile
    decks = profile.deck_set.all()
    folders = profile.folder_set.all()
    context = {'profile': profile, 'decks': decks, 'folders': folders}
    return render(request, 'users/profile.html', context)


@login_required(login_url='login')
def editProfile(request):
    user = request.user
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    username = profile.username

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            new_profile = form.save(commit=False)
            if new_profile.username != username:
                # Check if the new username is already in use
                if Profile.objects.filter(username=new_profile.username).exists():
                    messages.error(request, 'Username already exists')
                else:
                    # Save the profile if the username is unique
                    new_profile.save()
                    return redirect('profile')
            else:
                # Save the profile if the username hasn't changed
                new_profile.save()
                return redirect('profile')
        else:
            # Form is invalid, show errors
            messages.error(request, 'Invalid form submission')
    
    context = {'form': form, 'profile': profile}
    return render(request, 'users/edit-profile.html', context)


def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('decks')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('decks')
            
        # else:
        #     messages.error(request, 'Username or password is incorrect')
    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    users = User.objects.all()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            for user in users:
                if user.username != new_user.username:
                    new_user.username = new_user.username.lower()
                    new_user.save()
                    login(request, new_user)
                    return redirect('profile')
            else:
                print(user.username)
                messages.error(request, 'Username already exists')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)

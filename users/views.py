from django.shortcuts import render, redirect

# Create your views here.

def profile(request):
    context = {}
    return render(request, "users/profile.html", context)


def loginUser(request):
    context = {}
    return render(request, "users/login_register.html", context)

def logoutUser(request):
    logout(request)
    return redirect('login')
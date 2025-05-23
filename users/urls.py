from django.urls import path
from . import views

urlpatterns = [
    path('users', views.profile, name="profile"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]

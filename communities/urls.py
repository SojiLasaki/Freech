from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('communities/', views.communities, name = "communities"),
    path('create_community/', views.create_community, name="create_community"),
    path('circles/', views.circles, name = "circles"),
]

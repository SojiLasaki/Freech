from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('communities/', views.communities, name = "communities"),
    path('community', views.community, name = "community"),
    path('request_community/', views.request_community, name="request_community"),
    path('circles/', views.circles, name = "circles"),
    path('circle/<str:pk>/', views.circle, name ="circle"),
    path('convo/<str:pk>/', views.convo, name="convo"),
]

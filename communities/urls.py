from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('communities/', views.communities, name = "communities"),
    path('community', views.community, name = "community"),
    path('request_community/', views.request_community, name="request_community"),
    path('convo/<str:pk>/', views.convo, name="convo"),
    path('circles/', views.circles, name = "circles"),
    path('circle/<str:pk>/', views.circle, name ="circle"),
    path('circle_convo/<str:pk>/', views.circle_convo, name="circle_convo"),
    path('create_reply/', views.create_reply, name='create_deck'),
    path('create_convo/', views.create_convo, name="create_convo"),
    path('create_reply/', views.create_reply, name='create_reply'),
]

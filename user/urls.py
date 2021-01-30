from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/profile/', views.profile , name = 'profile'),
    #path('accounts/profile/view/', views.user_detail, name = 'user_detail'),
    path('accounts/profile/view', views.user_detail, name='user_detail'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('tutorial/', views.tutorial, name='tutorial'),
    path('python/', views.tutorialpython, name='tutorialpython'),
    path('cpp14/', views.tutorialcpp14, name='tutorialcpp14'),
    path('go/', views.tutorialgo, name='tutorialgo')
    	
]

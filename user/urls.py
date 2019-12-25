from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

app_name = 'user'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('accounts/profile/', views.profile , name = 'profile'),
    #path('accounts/profiles/(?P<id>\d+)', views.profiles , name = 'user_profile'),
]
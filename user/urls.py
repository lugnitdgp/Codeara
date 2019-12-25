from django.urls import path, include
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.home, name = 'home'),
]
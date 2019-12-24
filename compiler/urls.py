from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.code_editor, name="compiler"),
    path('result/', views.result, name="result"),
]
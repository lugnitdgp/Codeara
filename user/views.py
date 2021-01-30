from django.shortcuts import render
from google.oauth2 import id_token
from django.core.exceptions import ObjectDoesNotExist
from google.auth.transport import requests
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import os
from compiler.models import Question
from user.models import User_profile
from decouple import config
from allauth.socialaccount.models import SocialAccount


def home(request):
    ques = Question.objects.order_by('?').first()
    #ques = Question.objects.all()
    question = {"q_num":ques}
    return render(request,"home.html", question)

def profile(request):
    u_id = request.user.id

    try:
        obj = User_profile.objects.get(pk=u_id)

    except User_profile.DoesNotExist:
        obj = User_profile(pk=u_id)
        obj.first_name = request.user.first_name
        obj.user = request.user
        obj.save() 

    return render(request,'code_editor.html')

def user_detail(request):
    usr = User_profile.objects.get(pk=request.user.id)
    c_user = {"usr":usr}
    return render(request,'profile.html',c_user)


def leaderboard(request):
    p = User_profile.objects.order_by("-n_subm")
    users = {"user":p}
    return render(request,"leaderboard.html",users)
#Added by sahil
def tutorial(request):
	return render(request,"tutorial.html")


def tutorialpython(request):
	return render(request, "python.html")
	
def tutorialcpp14(request):
	return render(request, "cpp14.html")


def tutorialgo(request):
	return render(request, "go.html")
	



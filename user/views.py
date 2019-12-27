from django.shortcuts import render
from google.oauth2 import id_token
from django.core.exceptions import ObjectDoesNotExist
from google.auth.transport import requests
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import os
from compiler.models import Question
#from user.models import User
from decouple import config

def home(request):
    ques = Question.objects.order_by('?').first()
    #ques = Question.objects.all()
    question = {"q_num":ques}
    return render(request,"home.html", question)

def profile(request):
    #cur_user = request.User
    #usr = User.objects.get(id=cur_user.id)
    #usr = {"user":usr}
    return render(request,'code_editor.html')

def user_detail(request):
    #cur_user = request.user.get.id
    return render(request,'profile.html')



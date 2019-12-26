from django.shortcuts import render
from google.oauth2 import id_token
from django.core.exceptions import ObjectDoesNotExist
from google.auth.transport import requests
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import os
from compiler.models import Question
from decouple import config

def home(request):
    ques = Question.objects.order_by('?').first()
    #ques = Question.objects.all()
    question = {"q_num":ques}
    return render(request,"home.html", question)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('code_editor.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(requests):
    context = {}
    user = requests.user
    context['name']=user.username
    return render(requests,'code_editor.html')

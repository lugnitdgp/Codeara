from django.shortcuts import render
from google.oauth2 import id_token
from django.core.exceptions import ObjectDoesNotExist
from google.auth.transport import requests
from django.contrib.auth.models import User
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
import os
from compiler.models import Question
from user.models import User_profile
from decouple import config
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth.decorators import login_required

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

'''@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form}) '''



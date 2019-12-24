from django.shortcuts import render
from google.oauth2 import id_token
from django.core.exceptions import ObjectDoesNotExist
from google.auth.transport import requests
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.http import HttpResponse, JsonResponse
import os
from decouple import config

def home(request):
    return render(request,"home.html")

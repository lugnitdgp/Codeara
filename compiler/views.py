from django.shortcuts import render,HttpResponse
from django.conf import settings
import json
import requests
import base64
from django.contrib.auth.decorators import login_required
from user.models import User_profile

#new
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from user.models import User_profile
from django.forms import forms
from . import views
from django.views.generic import TemplateView



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'user/profile-update.html'

    def  post(self, request):

        post_data= request.POST or None
        file_data =  request.files or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was sucsessfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form, 
                                        profile_form=profile_form
                                    )
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request,**args, **kwargs)                                

        

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

client_id = "aa3c5e94ced8d771cb0a961ce09643e1"
client_secret = "300f819850eb030070e6e1e81eeb8cedfdb2d8445364d2801fb33bb4f647df83"

LANG_CODE = { 'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3,'go': 3,
            'sql': 3,'csharp': 3,'dart': 3,'nodejs': 3,'kotlin': 2,'brainfuck': 0,}


@login_required(login_url='/accounts/login/')
def code_editor(request):
    return render(request,'code_editor.html')


@login_required(login_url='/accounts/login/')
def result(request):
    if request.method == "POST":
        source = request.POST.get("script")
        lang = request.POST.get("lang")
        stdin = request.POST.get("stdin")
        u_id = request.user.id
        usr = User_profile.objects.get(pk=u_id)
        usr.n_subm += 1
        if check_lang(usr,lang):
            usr.lang +=lang+","
        usr.save()
        data = {'clientId':client_id,
                'clientSecret':client_secret,
                'script':source,
                'stdin':stdin,
                'language':lang,
                'versionIndex':LANG_CODE[lang],
            }
             
        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
            json_data = r.json()
            print(json_data)
            status = r.status_code
            print(status)
            #output = Robject(r.json())
            output = json_data['output']
            if not output:
                output = message.replace("\n","<br>")
        except Exception as e:
            print(e)
            output = settings.ERROR_MESSAGE
        print(output)   
        return HttpResponse(json.dumps({'output': json_data['output']}), content_type="application/json")
    else:
        return render(request,'code_editor.html',locals())


def check_lang(self,lang):
    lang_array = self.lang.split(",")
    for lng in lang_array:
        if lng == lang:
            return False
    return True            


'''
class Robject():
    def __init__(self, result):
        self.output = result['output']
        self.memory = result['memory']
        self.time = result['cpuTime']

'''
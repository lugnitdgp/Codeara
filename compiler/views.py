from django.shortcuts import render,HttpResponse
from django.conf import settings
import json
import requests
import base64

API_ENDPOINT = "https://api.jdoodle.com/v1/execute"

client_id = "aa3c5e94ced8d771cb0a961ce09643e1"
client_secret = "30ed01aa75f848fe6388516339bea7944295cfa0bb8f5983f7302e556c87b9bb"

LANG_CODE = { 'c': 1, 'java': 3, 'cpp14': 3, 'python3': 3}

def code_editor(request):
    return render(request,'code_editor.html')

def result(request):
    if request.method == "POST":
        source = request.POST.get("script")
        lang = request.POST.get("lang")
        stdin = [request.POST.get("stdin")]
        #print(source)
        data = {'clientId':client_id,
                'clientSecret':client_secret,
                'script':source,
                'language':"c",
                'versionIndex':"3",
            }
        #if 'stdin' in code:
            #data['stdin'] = stdin    
        try:
            headers = {'Content-type': 'application/json'}
            r = requests.post(url = API_ENDPOINT, data = json.dumps(data), headers = headers)
            json_data = r.json()
            status_code = r.status_code
            time = json_data['cpuTime']
            memory = json_data['memory']
            output = json_data['output']
            print(output)
            print(time)
            print(memory)
            if not output:
                output = message.replace("\n","<br>")
        except Exception as e:
            for i in range(10):
                print(e)
            output = settings.ERROR_MESSAGE
        #return HttpResponse(json.dumps({'output': output}), content_type="application/json")
        return HttpResponse(json_data)
    else:
        return render(request,'code_editor.html',locals())

'''
class Result():
    def __init__(self, result):
        self.output = result['output']
        self.memory = result['memory']
        self.time = result['cpuTime']

        
'''

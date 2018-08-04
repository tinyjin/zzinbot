from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):
  if request.method == "POST" :  
    message = {
      "message":{
          "text" : "안녕~? 나는 찐봇이야!"
      }
    }


    jsonObj = json.dumps(message, ensure_ascii=False)
    return HttpResponse(jsonObj, content_type = 'application/json; charset=utf-8')
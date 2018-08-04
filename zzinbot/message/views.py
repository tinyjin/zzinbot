from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

@csrf_exempt
def index(request):
  resChat = [
    '안녕~? 나는 찐봇이야!',
    '반가워~ 친구야~',
    '나랑.. 친구할래?',
    '나랑 놀자 ^^'
  ]

  if request.method == "POST" :  
    message = {
      "message":{
          "text" : random.choice(resChat)
      }
    }

    jsonObj = json.dumps(message, ensure_ascii=False)
    return HttpResponse(jsonObj, content_type = 'application/json; charset=utf-8')
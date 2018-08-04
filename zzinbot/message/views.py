from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import random

@csrf_exempt
def index(request):

  chat = [
    '안녕? 나는 찐봇이야!',
    '나는 너희들의 친구야~',
    '나랑 놀자~ ^^*',
    '나 심심행~'
  ]

  if request.method == "POST" :
    if request.POST['content'] == '찐봇이란?' :
      resChat = '찐봇은 2018년에 만들어진 대화형 로봇입니다.'
    else :
      resChat = random.choice(chat)

    message = {
      "message":{
          "text" : resChat
      }
    }

    jsonObj = json.dumps(message, ensure_ascii=False)
    return HttpResponse(jsonObj, content_type = 'application/json; charset=utf-8')
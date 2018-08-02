from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json


def index(request):
  message = {
    "message":{
        "text" : "안녕~? 나는 찐봇이야!"
    }
  }

  jsonObj = json.dumps(message, ensure_ascii=False)
  return HttpResponse(jsonObj, content_type = 'application/json; charset=utf-8')
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json


def index(request):
  buttons = {
    "type" : "buttons",
    "buttons" : ["찐봇이란?"]
  }

  jsonObj = json.dumps(buttons, ensure_ascii=False)
  return HttpResponse(jsonObj, content_type = 'application/json; charset=utf-8')
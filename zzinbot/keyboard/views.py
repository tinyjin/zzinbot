from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json


def index(request):
  buttons = {
    "type" : "buttons",
    "buttons" : ["블로그", "깃허브", "링크드인"]
  }

  jsonObj = json.dumps(buttons, ensure_ascii=False)
  return HttpResponse(jsonObj, content_type = 'application/json; charset=utf-8')
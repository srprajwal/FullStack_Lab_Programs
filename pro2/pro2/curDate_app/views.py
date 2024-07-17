from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta

def ahead4(request):
  now = datetime.now() + timedelta(hours = 4)
  res = "<h1>It will be - %s 4 hours later </h1>"%now
  return HttpResponse(res)

def behind4(request):
  now = datetime.now() - timedelta(hours = 4)
  res = "<h1>It was - %s 4 hours ago</h1>"%now
  return HttpResponse(res)
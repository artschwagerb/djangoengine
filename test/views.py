from django import http
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
#from google.appengine.api import urlfetch

def home(request):
	return http.HttpResponse('<head><link rel="icon" href="static/favicon.ico"></head><body><center><a href=https://www.google.com/search?q=scary+clown><img src=static/clown1.jpg></a></center></body>')
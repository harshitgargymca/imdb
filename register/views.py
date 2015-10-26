from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import requests
import json
from urllib import urlopen
def BaseLoginview(request):
	#if request.user.is_authenticated:
		#return HttpResponseRedirect('/profile')
	context={}
	return render_to_response('login.html',context, context_instance=RequestContext(request))

# Create your views here.

def my_view(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/profile')
	username = request.POST.get('username')
	password = request.POST.get('password')

	user = authenticate(username = username, password = password)
	print user
	if user is not None:
		if user.is_active:
			login(request, user)
			context = {}
			return render_to_response('profile.html',context, context_instance=RequestContext(request))

	else:
		return HttpResponseRedirect('/')

def registerview(request):
	username = request.POST['username_register']
	password1 = request.POST['password1']
	password2 = request.POST.get('confirm_password')
	if password1 and password2 and password1==password2:
		user = User.objects.create_user(username=username, password=password1)
		user.save()
		print user

		context = {}
	
		return render_to_response('profile.html',context, context_instance=RequestContext(request))

def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')

#@login_required
def profileview(request):
	context = {}
	return render_to_response('profile.html',context, context_instance=RequestContext(request))

def indexview(request):
	context ={}
	if request.method=="GET" and 'q' in request.GET:

		q=request.GET['q']
		if q is not None and q !='':
			url = urlopen("http://127.0.0.1:8000/api/v1/movie_detail/?pk="+q)
			data = url.read()
			data = json.loads(data)
			context = {'data':data}
			return render_to_response('index.html',context, context_instance=RequestContext(request))
	return render_to_response('index.html',context, context_instance=RequestContext(request))

def searchview(request):
	q=request.GET['q']
	url = urlopen("http://127.0.0.1:8000/api/v1/movie_detail/?pk="+q)
	data = url.read()
	data = json.loads(data)
	context = {'data':data}




	return render_to_response('index.html',context, context_instance=RequestContext(request))






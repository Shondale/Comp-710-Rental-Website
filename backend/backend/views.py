from django.shortcuts import render
from django.http import HttpResponse
#from .models import Name


def hello(request, name):
	#return render(request, "hello.html", {"name": name})
	return HttpResponse("<b>Hello " + name + "</b>")

def index(request):
	return render(request, "template/index.html")

def index(request):
	#return HttpResponse("<h2>You have reached the homepage</h2>")
	return render(request, "iRentals/index.html", {})

def appliances(request):
	pass

def electronics(request):
	pass

def furniture(request):
	pass

def tools(request):
	pass

def login(request):
	pass

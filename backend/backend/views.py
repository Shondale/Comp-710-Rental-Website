from django.shortcuts import render


def hello(request, name):
	return render(request, "hello.html", {"name": name})

	#return HttpResponse("<b>Hello " + name + "</b>")


def index(request):
	return render(request, "index.html")


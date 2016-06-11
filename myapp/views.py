from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, 'index.html')

def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})

def mcgill(request):
	return render(request, 'mcgill.html')

def pacificacademy(request):
	return render(request, 'pacificacademy.html')

def projects(request):
	return render(request, 'projects.html')

def datastructure(request):
	return render(request, 'datastructure.html')

def designpattern(request):
	return render(request, 'designpattern.html')

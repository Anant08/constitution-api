from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    #return render(request, 'index.html')
    return render(request, 'docu/home.html')

    #return HttpResponse("Hello! You're viewing the Constitution API. Its still in development, of course....")


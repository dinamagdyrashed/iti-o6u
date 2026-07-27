from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Login(request):
    return HttpResponse('<h1>Hi from login page</h1>')

def Register(request):
    return HttpResponse('<h1>Hi from register page</h1>')


def Logout(request):
    return HttpResponse('<h1>Hi from logout page</h1>')
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def allTracks(request):
    return HttpResponse('<p>We are in all tracks page</p>')


def gettrackbyid(request):
    return HttpResponse('<p>We are in track id</p>')


def updatetrack(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrack(request):
    return HttpResponse('<p>We are in delete track id</p>')
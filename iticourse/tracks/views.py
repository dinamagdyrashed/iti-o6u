from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def allTracks(request):
    tracks=[[1,'Django'],[2,'Odoo'],[3,'Flask']]
    return render(request,'tracks/list.html',context={'tracks':tracks})


def gettrackbyid(request,id):
    return HttpResponse(f'<p>We are in track {id}</p>')


def updatetrack(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrack(request,id):
    return HttpResponse(f'<p>We are in delete track {id}</p>')
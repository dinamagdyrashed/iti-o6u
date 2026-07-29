from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Track
def allTracks(request):
    context={'tracks':Track.objects.all()}

    return render(request,'tracks/list.html',context)


def gettrackbyid(request,id):
    return HttpResponse(f'<p>We are in track {id}</p>')


def updatetrack(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrack(request,id):
    return HttpResponse(f'<p>We are in delete track {id}</p>')

from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.http import HttpResponse

def allTrainee(request):
    return render(request,'trainee/trainee.html')


def gettraineebyid(request,id):
    return HttpResponse(f'<p>We are in trainee {id}</p>')


def updatetrainee(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrainee(request,id):
    return HttpResponse(f'<p>We are in delete trainee {id}</p>')

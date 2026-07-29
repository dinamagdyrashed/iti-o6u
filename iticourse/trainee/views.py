from django.shortcuts import render

# Create your views here.

# Create your views here.
from django.http import HttpResponse
from .models import Trainee
def allTrainee(request):
    context={'trainees': Trainee.objects.all()}
    return render(request,'trainee/trainee.html',context)


def inserttrainee(request):
    print('ddd',request.POST)
    if request.method=='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        Trainee.objects.create(name=name,email=email)
        return HttpResponse(f'<h1> Trainee {name} inserted successfully</h1>')
    return render(request,'trainee/insert.html')

def gettraineebyid(request,id):
    return HttpResponse(f'<p>We are in trainee {id}</p>')


def updatetrainee(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrainee(request,id):
    return HttpResponse(f'<p>We are in delete trainee {id}</p>')

from django.shortcuts import render,redirect

# Create your views here.

# Create your views here.
from django.http import HttpResponse
from .models import Trainee
def allTrainee(request):
    context={'trainees': Trainee.objects.all().order_by('id')}
    return render(request,'trainee/trainee.html',context)


def inserttrainee(request):
    print('ddd',request.POST)
    if request.method=='POST':
        name=request.POST['trname']
        email=request.POST['tremail']
        image=request.FILES['trimg']
        Trainee.objects.create(name=name,email=email,image=image)

        return redirect('/trainee/')
    return render(request,'trainee/insert.html')

def gettraineebyid(request,id):
    return HttpResponse(f'<p>We are in trainee {id}</p>')


def updatetrainee(request,id):
    return HttpResponse(f'<p>We are in update {id}</p>')

def deletetrainee(request,id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('/trainee/')

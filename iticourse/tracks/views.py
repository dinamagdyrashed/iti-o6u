from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import Track
def allTracks(request):
    context={'tracks':Track.objects.all().order_by('id')}

    return render(request,'tracks/list.html',context)

def inserttrack(request):
    if request.method=='POST':
        name=request.POST['trname']
        Track.objects.create(name=name)
        return redirect('/track/')
    return render(request,'tracks/insert_track.html')

def gettrackbyid(request,id):
    return HttpResponse(f'<p>We are in track {id}</p>')


def updatetrack(request,id):
    if request.method=='POST':
        Track.objects.filter(id=id).update(name=request.POST['trname'])
        return redirect('/track/')
        
    return render(request,'tracks/update_track.html',context={'track':Track.objects.get(id=id)})

def deletetrack(request,id):
    Track.objects.filter(id=id).delete()
    return redirect('/track/')

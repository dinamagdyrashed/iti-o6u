from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns=[
    path('',allTracks),
    path('insert/',inserttrack),
    path('id/<int:id>/',gettrackbyid),
    path('update/<int:id>/',updatetrack,name='updatetrack'),
    path('delete/<int:id>/',deletetrack,name='deletetrack'),
]
from django.contrib import admin
from django.urls import path,include

from .views import *
urlpatterns=[
    path('',allTracks),
    path('id/',gettrackbyid),
    path('update/<int:id>/',updatetrack),
    path('delete/',deletetrack),
]
from django.urls import path

from .views import *
urlpatterns=[
    path('',allTrainee),
    path('id/<int:id>/',gettraineebyid),
    path('update/<int:id>/',updatetrainee),
    path('delete/<int:id>/',deletetrainee),
]
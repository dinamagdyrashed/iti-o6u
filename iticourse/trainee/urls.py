from django.urls import path

from .views import *
urlpatterns=[
    path('',allTrainee),
    path('insert/',inserttrainee),
    path('id/<int:id>/',gettraineebyid),
    path('update/<int:id>/',updatetrainee,name='updatetrainee'),
    path('delete/<int:id>/',deletetrainee,name='deletetrainee'),
]
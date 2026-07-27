from django.contrib import admin
from django.urls import path

from .views import *
urlpatterns =[
    path('login/',Login),
    path('register/',Register),
    path('logout/',Logout),
]

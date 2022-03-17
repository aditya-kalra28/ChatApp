from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<str:room_name>/',views.room_func,name='room'),
    path('checkroom',views.checkroom,name='checkroom'),
    path('send',views.send,name='send'),
    path('getMessages/<str:room_name>/',views.getMessages,name='getMessages')
]


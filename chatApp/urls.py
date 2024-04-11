from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name='chathome'),
   path('checkroom',views.checkroom,name='checkroom'),
   path('<str:roomname>/',views.roomname,name='roomname'),
   path('send',views.send,name='send'),
   path('getmsg/<str:roomname>',views.getmsg,name='getmsg'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('edit/<id>',views.edit,name='edit'),
    path('del/<id>',views.dele,name="del"),
]

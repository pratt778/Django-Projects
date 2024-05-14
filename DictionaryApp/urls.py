from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='index'),
    path('wordpage',views.wordSearch,name='wordpage')
]

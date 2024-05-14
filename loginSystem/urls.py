from django.urls import path,include
from . import views
urlpatterns = [
    path('signup',views.signups),
    path('login',views.loginSys, name="login"),
    path('logout',views.logoutSys,name="logout"),
    path('logpage',views.logpage,name="logpage"),
]

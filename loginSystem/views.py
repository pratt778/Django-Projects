from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Logsystem
# Create your views here.

@login_required
def logpage(request):
    return render(request,'logpage.html')

def signups(request):
    data = {}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        passw = request.POST.get('password')
        conpass = request.POST.get('conpass')
        # print(name,email,passw,conpass)
        
        
        if name=='':
            info = "Name can't be Empty"
            data = {'ninfo':info}
            return render(request,'reg.html',data)
        if email=='':
            info = "Email can't be Empty"
            data = {'einfo':info}
            return render(request,'reg.html',data)
        if passw=='':
            info = "Password can't be Empty"
            data = {'pinfo':info}
            return render(request,'reg.html',data)
        if passw!=conpass:
            info = "Password didn't matched" 
            data = {'info':info}
            return render(request,'reg.html',data)
        if len(passw)<4:
            info = "Password is too short"
            data ={'sinfo':info}
            return render(request,'reg.html',info)
        if conpass=='':
            info = "Password can't be Empty"
            data = {'cinfo':info}
            return render(request,'reg.html',data)
        myuser = Logsystem.objects.create(name=name,email=email,password=passw)
        myuser.save()
        return redirect('login')
    return render(request,'reg.html')

def loginSys(request):
    if request.method =="POST":
        usern = request.POST.get('username')
        passw = request.POST.get('password')
        userauth = authenticate(username=usern,password=passw)
        if userauth is not None:
            login(request,userauth)
            return redirect('logpage')
    return render(request,'log.html')

def logoutSys(request):
    logout(request)
    return redirect('login')
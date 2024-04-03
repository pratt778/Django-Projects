import django
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str
from .tokens import token_generator

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    data={}
    if request.method == 'POST':
        name = request.POST.get('name')
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conpass = request.POST.get('conpass')
        if User.objects.filter(username=uname):
            msg = 'username already exists'
            data={'umsg':msg}
            return render(request,'signup.html',data)
        if User.objects.filter(email=email):
            emsg = 'email already exists'
            data = {'emsg':emsg}
            return render(request,'signup.html',data)
        if len(password)<3:
            lmsg='password too short'
            data = {'lmsg':lmsg}
            return render(request,'signup.html',data)
        if password!=conpass:
            pmsg="password didn't match"
            data ={'pmsg':pmsg}
            return render(request,'signup.html',data)
        myuser = User.objects.create_user(uname,email,password)
        myuser.first_name=name
        myuser.is_active=False
        myuser.save()
        messages.success(request,'Your account has been Successfully created !!!')

        #welcome emails sending

        subject = 'You have registered the account'
        strmsg='Welcome'+myuser.first_name+", you have successfully registered to the account"
        send_mail(subject,strmsg,'pratham016914934@gmail.com',[myuser.email],fail_silently=False)

        #account acitvation link 

        current_site= get_current_site(request)
        email_sub = 'Activating your email account'
        act_msg = render_to_string('activation.html',{
            'name':myuser.first_name,
            'domain':current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token_for_link': token_generator.make_token(myuser)
        })

        myemail = EmailMessage(
            email_sub,
            act_msg,
            'pratham016914934@gmail.com',
            [myuser.email]
        )
        myemail.fail_silently=False
        myemail.send()
        return redirect('signin')
    return render(request,'signup.html',data)


def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser=None
    if myuser is not None and token_generator.check_token(myuser,token):
        myuser.is_active=True
        myuser.save()
        login(request,myuser)
        name = myuser.first_name
        return render(request,'home.html',{'name':name})
    else:
        return render(request,'activationfailed.html')

def signin(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        passw = request.POST.get('password')
        userauth = authenticate(username=uname,password=passw)
        if userauth is not None:
            login(request,userauth)
            name= userauth.first_name
            return render(request,'home.html',{'name':name})
    return render(request,'signin.html')

def signout(request):
    logout(request)
    messages.success(request,'logged out successfully')
    return redirect('home')
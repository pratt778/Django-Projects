from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def emailsender(request):
    if request.method == 'POST':
        msg = request.POST.get('msg')
        sub = request.POST.get('sub')
        em = request.POST.get('email')
        send_mail(sub,msg,'pratham016914934@gmail.com',[em],fail_silently = False)
    return render(request,'emailsend.html')
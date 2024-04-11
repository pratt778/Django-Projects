from django.shortcuts import redirect, render
from django.http import HttpResponse,JsonResponse
from .models import Room,Message
# Create your views here.
def home(request):
    return render(request,'chathome.html')

def checkroom(request):
    if request.method=='POST':
        rname = request.POST.get('rname')
        uname = request.POST.get('uname')
        if Room.objects.filter(name=rname).exists():

            return redirect(rname+'/?username='+uname)
        else:
            new_room = Room.objects.create(name=rname)
            new_room.save()
            return redirect(rname+'/?username='+uname)

def roomname(request,roomname):
    username = request.GET.get('username')
    room_info = Room.objects.get(name=roomname)
    data={
        'username':username,
        'roomname':roomname,
        'room_info':room_info
    }
    return render(request,'room.html',data)

def send(request):
    message = request.POST['message']
    room_id = request.POST['room_id']
    username = request.POST['username']
    # print(message)
    new_msg = Message.objects.create(value=message,user=username,room=room_id)
    new_msg.save()
    return HttpResponse('message send successfully')

def getmsg(request,roomname):
    room_info = Room.objects.get(name=roomname)
    messages = Message.objects.filter(room=room_info.id)
    return JsonResponse({'msg':list(messages.values())})

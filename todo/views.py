from django.shortcuts import render,redirect
from .forms import todoform
from .models import todolist
# Create your views here.
def todo(request):
    form = todoform()
    mylist = todolist.objects.filter(user=request.user)
    data ={'form':form,'list':mylist}
    if request.method == 'POST':
        form = todoform(request.POST)
        if form.is_valid():
            newform = form.save(commit=False)
            newform.user = request.user
            newform.save()
            return redirect('todo')
    return render(request,'todo.html',data)

def edit(request,id):
    data={}
    mylist = todolist.objects.get(id=id)
    data['list']=mylist
    if request.method =='POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        mylist = todolist.objects.get(id=id)
        mylist.todoname=name
        mylist.tododesc = desc
        mylist.save()
        return redirect('todo')
    return render(request,'todoedit.html',data)

def dele(request,id):
    mylist = todolist.objects.get(id=id)
    mylist.delete()
    return redirect('todo')
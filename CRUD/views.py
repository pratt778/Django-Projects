from django.shortcuts import render,redirect
from .models import Employee
# Create your views here.
def employee(request):
    myinfo = Employee.objects.all()
    data = {'info':myinfo}
    return render(request,'emp.html',data)

def add(request):
    if request.method=="POST":
        name = request.POST.get('name')
        job = request.POST.get('job')
        # print(name)
        # print(job)
        myemp = Employee.objects.create(name=name,job=job)
        myemp.save()
    return redirect('employee')

def edit(request,eid):
    # print(ename)
    if request.method == 'POST':
        name = request.POST.get('name')
        job = request.POST.get('job')
        myemp = Employee.objects.get(id=eid)
        myemp.name=name
        myemp.job = job
        myemp.save()
        print('updated successfully')
        return redirect('employee')
    myinfo = Employee.objects.get(id=eid)
    data={'info':myinfo}
    return render(request,'update.html',data)

def delete(request,eid):
    mydel = Employee.objects.get(id=eid)
    mydel.delete()
    return redirect('employee')
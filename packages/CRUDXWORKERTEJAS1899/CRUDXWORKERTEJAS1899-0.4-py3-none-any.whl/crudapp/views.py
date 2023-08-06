from django.shortcuts import render
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def create(r):
    form = EmployeeForm()
    if r.method == 'POST':
        form = EmployeeForm(r.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    return render(r,'create.html',{"form":form})


def display(r):
    data = Employee.objects.all()
    return render(r,'display.html',{"data":data})

def delete(r,x):
    data = Employee.objects.get(eid=x)
    data.delete()
    return HttpResponseRedirect("/")

def update(r,y):
    data = Employee.objects.get(eid=y)
    if r.method == 'POST':

        form = EmployeeForm(r.POST,instance=data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")

    return render(r,'update.html',{"data":data})




from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/list.html', context)

@login_required(login_url='login')
def updateTask(request, pk):
    task = Task.objects.get(id=pk) 

    if request.method == "POST":
        form = TaskForm(data=request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = TaskForm(instance=task)
    context = {'form':form}
    return render(request, 'tasks/update_task.html', context)

@login_required(login_url='login')
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)

    if request.method == "POST":
        task.delete()
        return redirect('/')

    context = {'task':task}
    return render(request, 'tasks/delete.html', context)
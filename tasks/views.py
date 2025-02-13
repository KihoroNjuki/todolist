from django.shortcuts import render, redirect,get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description','')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request,'tasks/task_create.html')

def task_update(request,pk):
    task = get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        title= request.POST.get('title')
        description= request.POST.get('description','')
        completed= request.POST.get('completed',False)
        task.title = title
        task.description = description
        task.completed = completed
        task.save()
        return redirect('task_list')
    return render(request,'tasks/task_update.html',{'task': task})

def task_delete(request,pk):
    task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request,'tasks/task_confirm_delete.html',{'task': task})

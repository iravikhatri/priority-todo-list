from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import TaskForm

@login_required
def todolist(request):

    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        status = request.POST.get('status')
        task.status = status
        task.save()
        return redirect('todolist')

    context = {
        'tasks': Task.objects.all().order_by('-created_date')
    }
    return render(request, 'todolist/todolist.html', context)

@login_required
def detail_task(request, id):
    task = Task.objects.get(id=id)
    context = {
        'task': task
    }
    return render(request, 'todolist/detail_task.html', context)

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todolist')
    else:
        form = TaskForm()
    return render(request, 'todolist/create_task.html', {'form': form})

@login_required
def update_task(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        task.save()
        return redirect('detail_task', task.id)

    return render(request, 'todolist/update_task.html', {'form': form, 'task_id':task.id})

@login_required
def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()

    return redirect('todolist')

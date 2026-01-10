
from django.shortcuts import render,redirect
from .models import TODO_DB

# Create your views here.

def index(request):
    tasks = TODO_DB.objects.all()
    return render(request,"index.html",{'tasks': tasks})
def add_task(request):
    if request.method == 'POST':
        title=request.POST.get('task')
        print (title)
        TODO_DB.objects.create(title=title)
        return redirect('index')
    return render(request,"index.html")
def delete_task(request, task_id):
    TODO_DB.objects.filter(id=task_id).delete()
    return redirect('index')

def update_task(request, task_id):
    if request.method == 'POST':
        title=request.POST.get('task')
        TODO_DB.objects.filter(id=task_id).update(title=title)
        return redirect('index')
    return render(request,"update_task.html")
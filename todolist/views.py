from email import contentmanager
from multiprocessing import context
from django.shortcuts import render
import datetime

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from todolist.forms import taskForm
from todolist.models import Task
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers


@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_user = Task.objects.filter(user=request.user)
    context = {
        'username' : request.user.username,  
        'user_list' : data_user, 
    }
    return render(request, "mytodolist.html", context)


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login_user')
    
    context = {'form':form}
    return render(request, 'register_todolist.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login_todolist.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login_user')



#Add task user
@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == "POST":
        myform = taskForm(request.POST)
        if myform.is_valid():
            title = myform.cleaned_data["titles"]
            description = myform.cleaned_data["description"]
            # Task.objects.create(title=title, description=description, date=date, user=request.user)
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=request.user, is_finised="❌")

            return redirect('todolist:show_todolist')

    context = {
        'form' : taskForm()
    }
    return render(request, 'add_task.html', context)

def add_task_modal(request):
    if request.method == "POST":
        title_task = request.POST.get("title")
        description_task = request.POST.get('description')

        newTask = Task(title=title_task, description=description_task, date=datetime.datetime.now(), user=request.user, is_finised="❌")
        newTask.save()

        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()


def show_json(request):
    data_user = Task.objects.filter(user=request.user)
    return  HttpResponse(serializers.serialize('json', data_user))

# finish user
def finish_task(request, pk):
    mytask = Task.objects.get(id=pk)
    mytask.is_finised = "✅"
    mytask.save()
    return redirect('todolist:show_todolist')

def remove_task(request, pk):
    mytask = Task.objects.get(id = pk)
    Task.delete(mytask)
    return redirect('todolist:show_todolist')


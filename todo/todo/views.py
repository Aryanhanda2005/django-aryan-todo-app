from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from todo.models import TODOO

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        User.objects.create_user(fnm, email, password)
        return redirect('loginn')
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')
        user = authenticate(request, username=fnm, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('todo_page')   # ✅ match URL name
        else:
            return redirect('signup')
    return render(request, 'loginn.html')

def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TODOO.objects.create(title=title, user=request.user)
    tasks = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'tasks': tasks})

def edit_todo(request, srno):
    obj = get_object_or_404(TODOO, srno=srno, user=request.user)
    if request.method == 'POST':
        obj.title = request.POST.get('title')
        obj.save()
        return redirect('todo_page')   # ✅ match URL name
    tasks = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'edit_todo.html', {'obj': obj, 'tasks': tasks})

def delete(request, srno):   # ✅ renamed to match URL name
    obj = get_object_or_404(TODOO, srno=srno, user=request.user)
    obj.delete()
    return redirect('todo_page')

def complete(request, srno):   # ✅ renamed to match URL name
    task = get_object_or_404(TODOO, srno=srno, user=request.user)
    task.completed = True
    task.save()
    return redirect('todo_page')
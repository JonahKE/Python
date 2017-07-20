from django.shortcuts import render, HttpResponse, redirect

from models import *

# Create your views here.
def index(request):
    return redirect('/users')
def users(request):
    context = {
        'users': User.objects.all()
    }
    print context
    return render(request, 'users_app/index.html', context)
def new(request):
    return render(request, 'users_app/new.html')
def create(request):
    User.objects.create(name=request.POST['name'], email=request.POST['email'])
    return redirect('/users')
def show(request, number):
    if request.method == "POST":
        user = User.objects.get(id=number)
        user.name = request.POST['name']
        user.email = request.POST['email']
        user.save()
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request, 'users_app/show.html', context)
def edit(request, number):
    context = {
        'user': User.objects.get(id=number)
    }
    return render(request, 'users_app/edit.html', context)
def destroy(request, number):
    User.objects.get(id=number).delete()
    return redirect('/users')

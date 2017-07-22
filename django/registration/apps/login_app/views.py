from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User
from datetime import datetime
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'login_app/index.html')
def add(request):
    errors = User.objects.validation(request.POST)
    if errors > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=pwhash)
        request.session['first_name'] = request.POST['first_name']
        return redirect('/success')
def check(request):
    errors = User.objects.login_validation(request.POST)
    if len(errors) > 0:
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
        return redirect('/success')

def success(request):
    return render(request, 'login_app/success.html')

def logout(request):
    request.session.clear()
    return redirect('/')

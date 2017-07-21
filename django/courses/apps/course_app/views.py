from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages
# Create your views here.
def index(request):
    content = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_app/index.html', content)
def process(request):
    errors = Course.objects.validation(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
    else:
        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')
def destroy(request, number):
    content = {
        'course': Course.objects.get(id=number)
    }
    return render(request, 'course_app/destroy.html', content)
def confirm(request, number):
    Course.objects.get(id=number).delete()
    return redirect('/')

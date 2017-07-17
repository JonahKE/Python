from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    response = "placeholder to later display all the list of blogs"
    return HttpResponse(response)
def new(request):
    reponse = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)
def create(request):
    return redirect('/blogs')
def show(request, number = "1"):
    response="placeholder to display blog ", number
    return HttpResponse(response)
def edit(request, number = "1"):
    response="placeholder to edit blog ", number
    return HttpResponse(response)
def destroy(request):
    return redirect('/blogs')
def addnew(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

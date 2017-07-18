from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
    return render(request, 'sf/index.html')
def process(request):
    if request.method == "POST":
        print request.POST
        request.session['count'] += 1
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['lang'] = request.POST['lang']
        request.session['comment'] = request.POST['comment']
        return redirect('/result')
    else:
        return redirect('/')
def result(request):
    return render(request, 'sf/result.html')

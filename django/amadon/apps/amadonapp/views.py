from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request, 'amadonapp/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['product_id'] == '1':
            quantity = int(request.POST['quantity'])
            charge = quantity * 19.99
            request.session['charge'] = charge
        elif request.POST['product_id'] == '2':
            quantity = int(request.POST['quantity'])
            charge = quantity * 29.99
            request.session['charge'] = charge
        elif request.POST['product_id'] == '3':
            quantity = int(request.POST['quantity'])
            charge = quantity * 4.99
            request.session['charge'] = charge
        elif request.POST['product_id'] == '4':
            quantity = int(request.POST['quantity'])
            charge = quantity * 49.99
            request.session['charge'] = charge

        if not 'item_count' in request.session:
            request.session['item_count'] = 0
        count = request.session['item_count']
        count += quantity
        request.session['item_count'] = count

        if not 'total_charge' in request.session:
            request.session['total_charge'] = 0
        total_charge = request.session['total_charge']
        total_charge += charge
        request.session['total_charge'] = total_charge
        return redirect('/checkout')
    else:
        return redirect('/')

def checkout(request):
    return render(request, 'amadonapp/checkout.html')

def reset(request):
    request.session.clear()
    return redirect('/')

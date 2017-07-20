from django.shortcuts import render, HttpResponse, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
    if not 'gold' in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
    if request.session['gold'] < 0:
        request.session['gold'] = 0
    return render(request, 'gold/index.html')

def process(request, location):
    if request.method == 'POST':
        if location == 'farm':
            gold = random.randint(10,20)
            request.session['gold'] += gold
            request.session['activities'].append('Earned {} golds from the farm! {}'.format(gold,datetime.now().strftime("%m/%d/%Y %I:%M %p")))
        if location == 'cave':
            gold = random.randint(5,10)
            request.session['gold'] += gold
            request.session['activities'].append('Earned {} golds from the cave! {}'.format(gold,datetime.now().strftime("%m/%d/%Y %I:%M %p")))
        if location == 'house':
            gold = random.randint(2,5)
            request.session['gold'] += gold
            request.session['activities'].append('Earned {} golds from the house! {}'.format(gold,datetime.now().strftime("%m/%d/%Y %I:%M %p")))
        if location == 'casino':
            gold = random.randint(0,50)
            win_lose = random.randint(0,1)
            if win_lose == 0:
                request.session['gold'] += gold
                request.session['activities'].append('Earned {} golds from the casino! {}'.format(gold,datetime.now().strftime("%m/%d/%Y %I:%M %p")))
            else:
                request.session['gold'] -= gold
                request.session['activities'].append('Lost {} golds from the casino! {}'.format(gold,datetime.now().strftime("%m/%d/%Y %I:%M %p")))
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

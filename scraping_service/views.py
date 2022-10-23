from unicodedata import name
from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now().date()
    name = 'Maksim'
    _context = {'date': date, 'name':name}
    return render(request, 'home.html', _context)
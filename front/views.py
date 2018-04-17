from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'front/about.html', {})

def contact(request):
    context = {
        'street': '1109 12th St E',
        'city': 'Saskatoon',
        'country': 'Canada',
        'phone': '3063618117',
        'email': 'jennifer@playsask.com'
    }
    return render(request, 'front/contact.html', context)

def about(request):
    return render(request, 'front/about.html', {})
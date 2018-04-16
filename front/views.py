from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<html><style>h1 {font-size: 72px; color: red; border: 1px solid blue;} ul {display: inline; list-style: none;}</style><ul>Links<li><a href='./about'>About</a></li><li><a href='./contact'>Contact</a></li></ul><h1>My page</h1><div><img width=500 src='https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg' /> </div></html>")

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
from django.http import HttpResponse


def index(request):
    return HttpResponse("<html><style>h1 {font-size: 72px; color: red; border: 1px solid blue;} ul {display: inline; list-style: none;}</style><ul>Links<li><a href='www.google.com'>About</a></li><li><a href='#'>Contact</a></li></ul><h1>My page</h1><div><img width=500 src='https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg' /> </div></html>")
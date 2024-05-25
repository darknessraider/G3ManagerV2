from django.shortcuts import HttpResponse, HttpResponseRedirect, render 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest


def login_user(request: HttpRequest):
    if request.method != 'POST':
        return render(request, 'authenticate/login.html', {})

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is None:
        return HttpResponse('<h1>Invalid Login</h1>')

    login(request, user)
    return HttpResponseRedirect('/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')



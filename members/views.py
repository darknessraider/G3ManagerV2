from django.shortcuts import HttpResponse, HttpResponseRedirect, render 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from .forms import UserSignupForm


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


def signup_user(request):
    if request.method != 'POST':
        form = UserSignupForm()
        return render(request, 'authenticate/signup.html', {'form': form})
   
    form = UserSignupForm(request.POST)

    if not form.is_valid():
        return HttpResponse('<h1>Error With Form Validation</h1>')
   
    data = form.cleaned_data

    if data['password'] != data['confirm_password']:
        return HttpResponse('<h1>Password And Confirm Password Do Not Match</h1>')

    user = User.objects.create_user(data['username'], data['email'], data['password'])
    user.save()
    return HttpResponseRedirect('/')


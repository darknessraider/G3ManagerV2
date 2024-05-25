from django.shortcuts import render 

def index(request):
    return render(request, 'home/home.html', {'username': request.user.username})


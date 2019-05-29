from django.shortcuts import render, get_object_or_404, redirect
from .models import Notice
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def home(request):
    return render(request, 'homepage/home.html')

def about(request):
    return render(request, 'homepage/about.html')

def map(request):
    return render(request, 'homepage/map.html')

def collection(request):
    return render(request, 'homepage/collection.html')

def notice(request):
    notices = Notice.objects.all()
    return render(request, 'homepage/notice.html', {'notices':notices})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'homepage/login.html', {'error':'ID or password is incorrect'})
    else:
        return render(request, 'homepage/login.html')
    return render(request, 'homepage/login.html')

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'homepage/signup.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
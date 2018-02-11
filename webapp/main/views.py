import os
from .models import Responses
from django.http import HttpResponse
from django.views.static import serve
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))
def get_link(season, episode):
    return "foo"

@csrf_exempt
def savecsv(request):
    if(request.method == 'POST'):
        jsondat = request.POST['jsondata']
        username = request.user.username
        a = Responses()
        a.username = username
        a.jsonString = jsondat
        a.save()
    return redirect('/')

@csrf_exempt
def index(request):
    if request.user.is_active == False:
        return redirect('/login')    
    if(request.method == 'POST'):
        season = request.POST['season']
        episode = request.POST['episode']
        vidlink = get_link(season, episode)
        print(season, episode)
        csvfile = ""
        with open(os.path.join(BASE_DIR, "main.csv"), "r") as f:
            csvfile = f.read()
        print(csvfile)
        return render(request, 'main/index.html', {'season' : int(season), 'episode' : int(episode), 'vidlink' : vidlink, "csv" : csvfile, "username" : str(request.user.username)})
    
    return render(request,'main/index.html', {'season' : "-1", 'episode' : "-1", 'vidlink' : "none", "csv" : "none", "username" : "none" })

@csrf_exempt
def signin(request):
    if request.user.is_active == True :
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        user = authenticate(username = user_name, password = password)
        if user == None :
            return render(request, 'main/login.html', {'error' : 'User-Name/Password Invalid'})
        elif user.is_active == False :
            login(request, user)
            return redirect('/')
        else : 
            login(request, user)
            return redirect('/')
    
    return render(request, 'main/login.html', None)

@csrf_exempt
def register(request):
    if request.user.is_active == True:
        return redirect('/')

    if request.method == 'POST':
        user_name = request.POST['user_name']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        user = User.objects.create_user(username=user_name, email=email, password=password, first_name=first_name, last_name=last_name)
        if user == None :
            return render('main/register.html', {'error' : "Authentication Error, Please Try Again."})

        user.is_active = True
        user.save()
        login(request, user)
        return redirect('/')
    return render(request, 'main/register.html', None)

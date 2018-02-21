import os
from .models import Responses
from django.http import HttpResponse
from django.views.static import serve
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404

BASE_DIR = os.path.dirname((os.path.dirname(os.path.abspath(__file__))))

csvfile = ""
with open(os.path.join(BASE_DIR, "main.csv"), "r") as f:
    csvfile = f.read()

@csrf_exempt
def savecsv(request):
    if(request.method == 'POST'):
        jsondat = request.POST['jsondata']
        last_id = request.POST['last_id']
        a = Responses.objects.get(user=request.user)
        a.jsonString += jsondat
        a.lastId = last_id
        a.save()
    return redirect('/')

@csrf_exempt
def index(request):
    if request.user.is_active == False:
        return redirect('/login') 

    a = Responses.objects.get(user=request.user)
    return render(request, 'main/index.html', {"csv" : csvfile, "username" : str(request.user.username), "status" : "Ready for S01", "last_id" : a.lastId, "jsondat" : a.jsonString})    


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

        try:
            user = User._default_manager.get(username__iexact = user_name.lower())
            return render(request, 'main/login.html', {'error':'User-Name Already Exists'})
        except User.DoesNotExist:
            user = User.objects.create_user(username=user_name.lower(), email=email, password=password, first_name=first_name, last_name=last_name)
            if user == None :
                return render('main/register.html', {'error' : "Authentication Error, Please Try Again."})
            user.is_active = True
            user.save()
            response = Responses()
            response.user = user
            response.lastId = 0
            response.save()
            user = authenticate(username = user_name, password = password)
            login(request, user)
        return redirect('/')
    return render(request, 'main/register.html', None)

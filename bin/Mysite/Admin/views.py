from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from datetime import datetime
from login import models
import serials

def LoginAdminView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user and user.username == '9017313196' and user.password == 'pbkdf2_sha256$180000$PFdQMmCaJqev$hggQqewZvKHXXH+Ths3h7TWViFbBWKCjp1r3jv8shAw=':
            request.session.set_expiry(0)
            request.session['username'] = request.user.username
            request.session.save()
            response = HttpResponse(request, 'Login.html')
            response.set_cookie('username',request.user.username)
            login(request, user)
            return redirect('/Home')
        else:
            return render(request, 'Login.html', {'error': 'Username or Password incorrect.'})
    else:
        return render(request, 'Login.html')

def HomeAdminView(request):
    if not request.user.is_active :
        return HttpResponse("<h1>sorry!you should be log in !</h1>")
    if request.user.is_active :
        return render(request,'Home.html')

def InformationsView(request):
    now = datetime.now()
    for l in models.Information.objects.all():
        time = l.date
        now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
        time = datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
        period = now - time
        period = str(period)
        models.Information.objects.filter(username = l.username).update(time = period)
    info = models.Information.objects.all()
    return render(request,'Informations.html',{'info' : info})

def SerialsView(request):
    srl = serials.models.Serials.objects.all()
    return render(request,'Serials.html',{'srl' : srl})

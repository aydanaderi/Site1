from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from . import models,forms

def SignupView(request):
    help_text = "please enter your phone number like 9--------- !"
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username = user.username, password = raw_password)
            request.session.set_expiry(0)
            request.session['username'] = request.user.username
            request.session.save()
            response = HttpResponse(request, 'login.html')
            response.set_cookie('username',request.user.username)
            db = models.Logindb.objects.all()
            password = make_password(raw_password)
            db = models.Logindb.objects.create(username = user.username, password = password)
            db.save()
            login(request, user)
            return redirect('/home')
    else:
        form = forms.SignUpForm()
    return render(request, 'signup.html', {'form': form,'help_text' : help_text})

def LoginView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user:
            request.session.set_expiry(0)
            request.session['username'] = request.user.username
            request.session.save()
            response = HttpResponse(request, 'login.html')
            response.set_cookie('username',request.user.username)
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'login.html', {'error': 'Username or Password incorrect.'})
    else:
        return render(request, 'login.html')

def HomeView(request):
    if not request.user.is_active :
        return HttpResponse("<h1>sorry!you should be log in !</h1>")
    if request.user.is_active :
        return render(request,'home.html')
def UserView(request):
        list = []
        for l in models.Logindb.objects.all():
            list.append(l.username)
            list.append(l.password)
        return JsonResponse(list ,safe = False)

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from . import models,forms

def SignupView(request):
    help_text = "enter a phone number like 9---------"
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
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            password = ''
            for i in raw_password :
                position = alphabet.find(i)
                newposition = (position + 5) % 62
                password += alphabet[newposition]
                                                                                                #data base
            db = models.Logindb.objects.create(username = user.username, password = password)
            db.save()
                                                                                                #end
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
        context = {}
        if request.method == 'POST':
            uploaded_file = request.FILES['document']
            fs = FileSystemStorage()
            name = fs.save(uploaded_file.name,uploaded_file)
            context['url'] = fs.url(name)                                                                                        #data base
            im = models.Documents.objects.create(docfile = fs.url(name))
            im.save()
        context['username'] = request.user.username
        return render(request,'home.html',context)

def UserView(request):
        list = []
        for l in models.Logindb.objects.all():
            list.append(l.username)
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            password = ''
            for i in l.password :
                pos = alphabet.find(i)
                newpos = (pos - 5) % 62
                password += alphabet[newpos]
            list.append(password)
        return JsonResponse(list ,safe = False)
                                                                                                                                                                                                           #data base
def AddressView(request):
        list = []
        for d in models.Documents.objects.all():
            docfile = str(d.docfile)
            list.append(docfile)
        return JsonResponse(list ,safe = False)
                                                                                                #end
def BasicView(request):
    return render(request, 'basic.html')

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
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
            email = form.cleaned_data.get('email')
            user.save()
            user = authenticate(username = user.username, password = raw_password , email = 'email')
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
            date = datetime.now()                                                                                    #data base
            db = models.Information.objects.create(username = user.username, password = password,date = date,email = email)
            db.save()
            subject = 'Signed up'
            message = 'hello! welcom to our site. your sign up was successful'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email,]
            send_mail( subject, message, email_from, recipient_list )                                                                        #end
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
            context['url'] = fs.url(name)
            inf = models.Information.objects.filter(username = request.user.username).update(profile = fs.url(name))                  #data base
        context['username'] = request.user.username
        email = ""
        for l in models.Information.objects.all():
            username1 = str(l.username)
            username2 = str(request.user.username)
            if username1 == username2:
                email = l.email
                break
        context['email'] = email
        return render(request,'home.html',context)

def UserView(request):
        list = []
        now = datetime.now()
        for l in models.Information.objects.all():
            list.append(l.username)
            alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
            password = ''
            for i in l.password :
                pos = alphabet.find(i)
                newpos = (pos - 5) % 62
                password += alphabet[newpos]
            list.append(password)
            list.append(l.date)
            time = l.time
            now = datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)
            time = datetime(time.year, time.month, time.day, time.hour, time.minute, time.second)
            period = now - time
            list.append(str(period))
            list.append(l.email)
            profile = str(l.profile)
            list.append(profile)
        return JsonResponse(list ,safe = False)
                                                                                                #end
def BasicView(request):
    return render(request, 'basic.html')

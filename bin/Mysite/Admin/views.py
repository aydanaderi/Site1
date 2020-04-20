from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def LoginAdminView(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        print(request.user.username)
        print(request.user.password)
        if user and user.username == '9017313196' and user.password == 'pbkdf2_sha256$180000$PFdQMmCaJqev$hggQqewZvKHXXH+Ths3h7TWViFbBWKCjp1r3jv8shAw=':
            request.session.set_expiry(0)
            request.session['username'] = request.user.username
            request.session.save()
            response = HttpResponse(request, 'loginadmin.html')
            response.set_cookie('username',request.user.username)
            login(request, user)
            return redirect('/homeadmin')
        else:
            return render(request, 'loginadmin.html', {'error': 'Username or Password incorrect.'})
    else:
        return render(request, 'loginadmin.html')

def HomeAdminView(request):
    if not request.user.is_active :
        return HttpResponse("<h1>sorry!you should be log in !</h1>")
    if request.user.is_active :
        return render(request,'homeadmin.html')

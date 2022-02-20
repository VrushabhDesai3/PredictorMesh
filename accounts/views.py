from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

def register(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        cpass = request.POST['cpass']

        if password == cpass:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username Taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=uname, password=password, email=email, first_name=fname, last_name=lname)
                user.save()
                return redirect('login')

        else:
            messages.error(request, 'Password not matching...')
            return redirect('register')
        return redirect('/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['pass']

        user = auth.authenticate(username=uname, password=password)

        if user is not None:
            auth.login(request, user)
            print('Logged In!')
            return redirect('/',)
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if username == "":
            messages.info(request, "Enter your username")
        elif password == "":
            messages.info(request, "Enter your password")
        else:
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            else:
                messages.info(request, "Invalid credentials")
                return redirect('login')

    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if username == "":
            messages.info(request, "Enter your username")
        elif password == "":
            messages.info(request, "Enter your password")
        elif password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                print("user created")
                return redirect('login')
        else:
            messages.info(request, "password not matching")
            return redirect('register')
        # return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

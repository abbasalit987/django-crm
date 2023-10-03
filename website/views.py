from django.shortcuts import render, redirect
# django authentication system
from django.contrib.auth import authenticate, login, logout
# django messaging system
from django.contrib import messages

# Create your views here.


def home(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.success(request, "Error logging in, please try again...")
            return redirect('home')
    else:
        return render(request, 'home/index.html', {})


# def loginUser(request):
#     pass


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


def registerUser(request):
    return render(request, 'register/register.html', {})

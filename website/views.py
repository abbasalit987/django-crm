from django.shortcuts import render, redirect
# django authentication system
from django.contrib.auth import authenticate, login, logout
# django messaging system
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()
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
        return render(request, 'home/index.html', {'records': records})


# def loginUser(request):
#     pass


def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')


def registerUser(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "Registration is successfull!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register/register.html', {'form': form})

    return render(request, 'register/register.html', {'form': form})

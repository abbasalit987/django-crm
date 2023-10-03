from django.shortcuts import render, redirect
# django authentication system
from django.contrib.auth import authenticate, login, logout
# django messaging system
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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


def customerRecord(request, pk):
    if request.user.is_authenticated:
        customerRecord = Record.objects.get(id=pk)
        return render(request, 'record/record.html', {'customerRecord': customerRecord})
    else:
        messages.success(request, "Please login to view record")
        return redirect('home')


def deleteRecord(request, pk):
    if request.user.is_authenticated:
        toDelete = Record.objects.get(id=pk)
        toDelete.delete()
        messages.success(request, "Record deleted successfully!")
        return redirect('home')
    else:
        messages.success(request, "Please login to view record")
        return redirect('home')


def addRecord(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'record/add-record.html', {'form': form})
    else:
        messages.success(request, "Please login to view record")
        return redirect('home')


def editRecord(request, pk):
    if request.user.is_authenticated:
        currentRecord = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=currentRecord)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated successfully!")
            return redirect('home')
        return render(request, 'record/edit-record.html', {'form': form})
    else:
        messages.success(request, "Please login to view record")
        return redirect('home')

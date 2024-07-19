from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been Log In"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please Try Again"))
            return redirect('login')
    else:   
        return render(request, 'login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Log Out Successfully!"))
    return redirect('home')
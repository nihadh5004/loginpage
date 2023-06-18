from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    return redirect('signin')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user = authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
             messages.error(request,'Incorrect Username or Password!')
             return redirect('signin')
    
    return render(request,'signin.html')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    if request.user.is_authenticated:
        logout(request)
    
    messages.success(request,"logged Out successfully")
    return redirect('signin')

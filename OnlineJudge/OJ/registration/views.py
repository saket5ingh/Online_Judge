from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import Problem

# Create your views here.
def home(request):
    return render(request,"registration/index.html")

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        verify_password=request.POST['verify_password']

        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name 

        myuser.save()

        messages.success(request,"Your account has been successfully")
        return redirect('signin')

    return render(request,"registration/signup.html")

def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            first_name=user.first_name
            problems = Problem.objects.all()
            return render(request, 'problem/list.html', {'problems': problems})
        
        else:
           messages.error(request,"Bad Credentials!")
           return redirect('home') 
    return render(request,"registration/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"Logged Out Successfully!")
    return redirect('home')

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'problem/problem_list.html', {'problems': problems})

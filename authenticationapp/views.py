from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def homeregistration(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save();
        return redirect('authlogin')
    return render(request,'registration.html')


def authlogin(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=name,password=password)
        if user is not None:
            login(request,user)
            return redirect('homeachievement')
        else:
            messages.error(request,"Invalid Password!")
        
    return render(request,'login.html')

def userlogout(request):
        logout(request)
        return redirect('home')

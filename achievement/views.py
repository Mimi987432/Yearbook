from django.shortcuts import render
from .models import student
from achievement import views

def homeachievement(request):
    return render(request,'achievehome.html')

def seeachievement(request):
    stdata=student.objects.all()
    context={
        'seedata':stdata
    }
    return render(request,'seeachieve.html',context)

def addachievement(request):
    if request.method=='POST':
        name=request.POST.get('name')
        department=request.POST.get('department')
        roll=request.POST.get('roll')
        email=request.POST.get('email')
        facebook=request.POST.get('facebook')
        address=request.POST.get('address')
        about=request.POST.get('about')

        studentdata=student(name=name,department=department,roll=roll,email=email,facebook=facebook,address=address,about=about)
    
        studentdata.save()
    return render(request,'achieveadd.html')

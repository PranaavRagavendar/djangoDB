from django.shortcuts import render,redirect
from.models import Member,Login
from .forms import MemberForm,LoginForm
from django.contrib import messages

def home(request):
    return render(request,'home.html',{})

def status(request):
    all_members = Member.objects.all
    return render(request,'status.html',{'all':all_members})

def attendance(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
          form.save()
        messages.success(request,('your form has been submitted successfully '))  
        return redirect('status')  
       
        
    else:
      return render(request,'attendance.html',{})
    
def login(request):
    if request.method == "POST":
       log = LoginForm(request.POST or None)
       if log.is_valid():
         log.save()
       messages.success(request,('login success'))  
       return redirect('user')  
    
    else:
       return render(request,'login.html',{})
     
     
     
def user(request):
    all_user = Login.objects.all
    return render(request,'user.html',{'all1':all_user})     
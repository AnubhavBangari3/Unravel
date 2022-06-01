from django.shortcuts import render,redirect
from django.http import JsonResponse

#user authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import Signupform

#message
from django.contrib import messages

# Create your views here.

def home(request):
    
    return render(request,"signin/base.html")

def sign(request):
    
    if request.method =='POST':
        username=request.POST.get('name')
        password=request.POST.get('password')
        user=authenticate(User,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login')
    context = {
        'user': User,
    }
    return render(request,"signin/sign.html")

def register(request):
    if request.method == 'POST':
        form=Signupform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            
            return redirect('login')
        else:
            messages.info(request,"Fil the details")
    else:
        form=Signupform()
        return render(request,"signin/register.html",{'form':form})
    
def logout_view(request):
    logout(request)
    return redirect('login')
            
            

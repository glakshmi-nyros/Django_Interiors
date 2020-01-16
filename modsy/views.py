
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.urls import reverse


# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse


from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages,auth
from modsy.forms import UserForm
from modsy.forms import UserRequirementForm
from django.contrib.auth import authenticate, login


from django import forms

from . models import room
from . models import goal
from . models import design
from . models import furniture
from . models import User_Requirement
from django.http import HttpResponseRedirect


# Create your views here.

# This view is for the home page
def index(request):
	return render(request, 'index.html',);

#This view is for the rooms page
def project1(request):
    rooms=room.objects.all()
    return render(request, 'rooms.html',{'room': rooms})

# This view is for the goals page
def project2(request):
    goals=goal.objects.all()
    return render(request, 'goals.html',{'goal':goals})

# This view is for the furniture page
def project3(request):
    f=furniture.objects.all()
    return render(request, 'furniture.html',{'furniture':f})

# This view is for the styles page
def project4(request):
    designs=design.objects.all()
    return render(request, 'styles.html',{'design':designs})

# This view is for register page
def home(request):
	return render(request,'register.html')
def dashboard(request):
    return render(request, 'dashboard.html',);


# This view is for storing all the steps of start a project wizard in the database
def user_register(request):
    if request.method == 'POST': # if there is a post request in the form
        user_form = UserForm(data=request.POST) #first of all it is a user_form will be posted details present in the user_form
        user_requirement_form = UserRequirementForm(data=request.POST)# after posting the details of the user_form post the details
        if user_form.is_valid() and user_requirement_form.is_valid():
         # if user_form & user_requirement form is valid
         
         User = user_form.save()#if form is valid save
         User.set_password(request.POST['password'])
         User.save()
         user_requirement = user_requirement_form.save(commit=False)
         # Set user
         user_requirement.user = User
         user_requirement.save()
         user_requirement_form.save_m2m()
         messages.success(request,('Project saved successfully'))
         return render(request,'home1.html')
        else:
          messages.warning(request, 'Please correct the errors above')
    else:  
        user_form = UserForm()
        user_requirement_form = UserRequirementForm()
    return render(request,'register.html', {'user_form': user_form, 'requirements_form': user_requirement_form})



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('modsy:dashboard'))
        
        else:
            messages.error(request,'Invalid Credentials')
            # return render(request,'dashboard.html') ## removed 1
    # else: ## removed 2
    return render(request, 'login.html')



def dashboard(request):
    return render(request, 'dashboard.html',);
def logout(request):
    messages.error(request,'You are now logged out')
    return render(request, 'login.html',);




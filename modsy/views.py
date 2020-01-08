
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse


from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from modsy.forms import UserForm
from modsy.forms import UserRequirementForm

from django import forms




from . models import room
from . models import goal
from . models import design
from . models import user
from . models import furniture
from . models import UserRequirement



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

# This view is for storing all the steps of start a project wizard in the database

def user_register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_requirement_form = UserRequirementForm(data=request.POST)
        if user_form.is_valid() and user_requirement_form.is_valid():
            user = user_form.save()
            user_requirement = user_requirement_form.save(commit=False)
            # Set user
            user_requirement.user = user
            user_requirement.save()
            user_requirement_form.save_m2m()
            return render(request,'register.html')
        else:
            messages.warning(request, 'Please correct the errors below')
    else:  
        user_form = UserForm()
        user_requirement_form = UserRequirementForm()
    return render(request,'register.html', {'user_form': user_form, 'requirements_form': user_requirement_form})

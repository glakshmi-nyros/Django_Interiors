
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# -*- coding: utf-8 -*-
from django.http import HttpResponse


from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from modsy.forms import UserForm
from django import forms




from . models import room
from . models import goal
from . models import design
from . models import user
from . models import furniture


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
        if user_form.is_valid():
            username=request.POST["username"]
            email = request.POST['email']
            password = request.POST['password']
            rooms = request.POST['room']
            g=goals=request.POST['goal']
            g = g.split(',')
            s=styles=request.POST['style']
            s=s.split(',')
            furn=request.POST['furn']
            u = user(username=username,password=password,email=email)
            u.rooms=room.objects.get(pk=rooms)
            goals = goal.objects.filter(pk__in=g)
            styles = design.objects.filter(pk__in=s)
            u.furn = furniture.objects.get(pk=furn)
            u.save()
            u.goals.add(*goals)
            u.styles.add(*styles)
            messages.success(request,'Your project design has been registered')
            return render(request,'register.html')
        else:
            messages.warning(request,'Cant be registered this email already exists')
            return render(request,'register.html')


        




	
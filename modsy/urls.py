from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name="modsy"

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    path('rooms/', views.project1, name='project1'),
    path('goals/', views.project2, name='project2'),
    path('furniture/', views.project3, name='project3'),
    path('styles/', views.project4, name='project4'),
    path('register/', views.home, name='home'),
    path('user_register/', views.user_register, name='user_register'),
    path('login/', views.login,name='login'),
    path('dashboard', views.dashboard,name='dashboard'),
    path('logout/', views.logout,name='logout')



]
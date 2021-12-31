from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [
     path('test/', views.test),
     path('login/', views.login),
     path('logout/', views.logout),
     path('my_publish/', views.my_publish),
     path('signup/', views.signup),
]

from django.contrib import admin
from django.urls import path
from register import views
#register app urls
urlpatterns = [
    path('register',views.register,name='register'),    path('',views.login,name='login'),
    path('home',views.home,name='home'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profilefun,name='profile'),
]
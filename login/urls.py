from os import name
from django.contrib import admin
from django.urls import path, URLPattern
from . import views

urlpatterns = [
    path('',views.logdisp, name = 'logdisp'),
    path('reg',views.registerdisp, name = 'reg'),
    path('log',views.logindisp, name = 'log'),
    path('register',views.register, name = 'register'),
    path('login',views.login, name = 'login'),
    path('logout',views.logout, name = 'logout'),

]

# reg is the action name from logdisp.html
# registerdisp is the function name to be used in views

# log is the action name from logdisp.html
# logindisp is the function name to be used in views

# name =  is used to call the path if needed
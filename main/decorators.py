from django.shortcuts import render,get_object_or_404,redirect
from .models import *

def check_login(fun_c):
    def check_authentication(request):
        current_user = request.user
        if current_user.id != None:
            return redirect('main:home')
        else:
            return fun_c(request)
    return check_authentication

def login_required(fun_c):
    def authenticate(request):
        current_user = request.user
        if current_user.id != None:
            return fun_c(request)
        else:
            return redirect('main:login')
    
    return authenticate





    

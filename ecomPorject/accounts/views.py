from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your 

def userSignUp(request):
    if request.method == 'POST':
        fullName = request.POST.get('fname')
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = User.objects.create(
            first_name = fullName,
            username = username,
        )
        user.set_password(pass1)
        user.save()
        messages.success(request, "user register successfully")
        return redirect('user_login')
    
    return render(request, 'signUp.html')
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = authenticate(username = username, password = pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
            return redirect('userSignUp')
        
    return render(request, 'login.html')
    

        


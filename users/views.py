from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
# from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.urls import reverse
# from users.forms import CustomUserCreationForm
from .forms import LoginForm, RegisterForm
from django.contrib.auth.forms import PasswordChangeForm
# from django.http import JsonResponse
# Create your views here.

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('dwitter:dashboard')
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})
    
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                # messages.success(request, f'Hi {user.username.title()}, welcome back!')
                return redirect('dwitter:dashboard')
            # form is not valid or user is not authenticated
            else:
                messages.error(request,f'Invalid username or password. Try again!')
        return render(request,'users/login.html',{'form': form})

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('login') 

def sign_up(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": RegisterForm()}
        )
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.backend = "django.contrib.auth.backends.ModelBackend"
            user.save()
            # messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect(reverse("dwitter:dashboard"))
        else:
            return render(request, 'users/register.html', {'form': form})
        
def change_pass(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # To keep the user logged in
            return redirect('password_change_done')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/password_change_form.html', {'form': form})

def change_done(request):
    return render(request, 'users/password_change_done.html')

# def check_username(request):
#     username = request.GET.get(username)
#     data = {
#        'username_exists': User.objects.filter(username__iexact=username).exists()
#     }
#     return JsonResponse(data)
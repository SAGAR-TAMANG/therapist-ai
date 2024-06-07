from django.db import IntegrityError
from django.shortcuts import render, redirect
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
  msg = None

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      print("############### FORM BEGINS ###############")
      # username = form.cleaned_data.get("username")
      email = form.cleaned_data.get("email")
      password = form.cleaned_data.get("password")
      print(email)
      print(password)
      user = authenticate(email=email, password=password)
      print(user)
      if user:
        msg='Success'
        login(request, user)
        return redirect('index')
      else:
        msg='Fail'
    else:
      msg = "Error validating form. Please try again."
  else:
    form = LoginForm()
  
  return render(request, 'accounts/login.html', context={'form': form, 'msg': msg})

def register_user(request):
  msg = None
  
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')

        user = authenticate(email=email, password=password1)
        msg='User created. Please <a href="/login">login</a> instead.'
      except IntegrityError:
        msg='User already exists. Please <a href="/login">login</a> instead.'
    else:
      msg='Error validating form. Please try again.'
  
  form = SignUpForm()
  
  return render(request, 'accounts/register.html', context={'form': form, 'msg': msg})

def logout_view(request):
  logout(request)
  return redirect('index')
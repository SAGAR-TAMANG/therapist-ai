from django.db import IntegrityError
from django.shortcuts import render, redirect, HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

from dotenv import load_dotenv
import os

load_dotenv()

from google.auth.transport import requests
from google.oauth2 import id_token

# Create your views here.
def login_view(request):
  msg = None

  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      print("############### FORM BEGINS ###############")
      username = form.cleaned_data.get("username")
      # email = form.cleaned_data.get("email")
      password = form.cleaned_data.get("password")
      print(username)
      print(password)
      user = authenticate(username=username, password=password)
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

# Google OAuth

@csrf_exempt
def google_auth_receiver(request):
    """
    Google calls this URL after the user has signed in with their Google account.
    """
    token = request.POST.get('credential')

    print("Inside the auth receiver")

    if token:
        try:
            user_data = id_token.verify_oauth2_token(
                token, requests.Request(), os.environ['GOOGLE_OAUTH_CLIENT_ID']
            )
            # Assuming user_data contains the user's information (e.g., email)
            email = user_data.get('email')
            full_name = user_data.get('name')
            if email:
                # Try to authenticate the user
                user = authenticate(request, email=email)
                if user:
                    # User exists, log in the user
                    login(request, user)
                    return redirect('index')
                else:
                    # User doesn't exist, create a new user
                    username = email.split('@')[0] if not full_name else full_name.replace(" ", "_")
                    user = User.objects.create_user(username=username, email=email)
                    user.set_unusable_password()  # Since we're using Google OAuth, password isn't necessary
                    user.save()
                    login(request, user)
                    return redirect('index')
            else:
                # Email not found in user data, handle the error accordingly
                error_text = 'Email not provided in user data'
                return render(request, 'accounts/error.html', context={'error': error_text}, status=400)
        except ValueError:
            # Invalid token
            error_text = "Invalid token"
            return render(request, 'accounts/error.html', context={'error': error_text}, status=403)
    else:
        # Credential not provided in request, handle the error accordingly
        error_text = "Credential not provided"
        return render(request, 'accounts/error.html', context={'error': error_text}, status=400)

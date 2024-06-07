from django.shortcuts import render
from .forms import LoginForm, SignUpForm

# Create your views here.
def login_view(request):
  form = LoginForm()
  return render(request, 'accounts/login.html', context={'form': form})

def register_user(request):
  form = SignUpForm()
  
  return render(request, 'accounts/register.html', context={'form': form})
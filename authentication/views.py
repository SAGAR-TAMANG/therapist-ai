from django.shortcuts import render
from .forms import LoginForm, SignUpForm

# Create your views here.
def login_view(request):
  return render(request, 'accounts/login.html')

def register_user(request):
  form = SignUpForm()
  
  return render(request, 'accounts/register.html', context={'form': form})
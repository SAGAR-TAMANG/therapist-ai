from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField
# from .models import CustomUser

class LoginForm(forms.Form):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Username',
        'class': 'form-control mb-2',
        'autocomplete': 'current-username',
      }
    )
  )
  password = forms.CharField(
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Password',
        'class': 'form-control mb-2',
        'autocomplete': 'current-password',
      }
    )
  )
  # captcha = ReCaptchaField()

class SignUpForm(UserCreationForm):
  username = forms.CharField(
    widget=forms.TextInput(
      attrs={
        'placeholder': 'Username',
        'class': 'form-control mb-2',
        'autocomplete': 'new-username',
      }
    )
  )
  email = forms.EmailField(
    label='Email',
    widget=forms.EmailInput(
      attrs={
        'placeholder': 'Give your email',
        'class': 'form-control mb-2',
        'autocomplete': 'email',
      }
    )
  )
  password1 = forms.CharField(
    label='Password',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Password',
        'class': 'form-control mb-2',
        'autocomplete': 'new-password',
        }
    )
  )
  password2 = forms.CharField(
    label='Confirm Password',
    widget=forms.PasswordInput(
      attrs={
        'placeholder': 'Confirm your password',
        'class': 'form-control mb-2',
        'autocomplete': 'new-password',        
      }
    )
  )
  # captcha = ReCaptchaField()

  class Meta:
    model = User
    # fields = ('username', 'email', 'password1', 'password2', 'captcha')
    fields = ('username', 'email', 'password1', 'password2')